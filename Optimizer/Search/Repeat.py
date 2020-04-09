#!/usr/bin/env python3
"""multi acquisition Search algorithm."""

__author__ = "R.Nakata"
__date__ = "2020/02/14"


from logging import getLogger
from typing import List, Tuple

import numpy as np
from mypythontools.Design import Singleton

from Models.GPR import GPR
from Models.ModelInterface import BayesianModelInterface

from ..Sampling.Random import RandomSampling
from .Acquisition.EHVI import EHVI
from .Acquisition.EI import EI
from .EHVISearch import EHVISearch
from .Scalarization.PBI import PBI
from .Scalarization.ScalarizationInterface import ScalarizationInterface
from .Scalarization.WeightVector import UniformalWeight
from .SearchInterface import SearchInterface

logger = getLogger()


class RepeatAlgorithm(Singleton):
    """
    multi acquisition Search algorithm.
    """

    def calculateGoodWeightList(
        self, popX: List[np.ndarray], popY: List[np.ndarray], goodIndiv: np.ndarray
    ) -> List[Tuple[float, BayesianModelInterface, float, int]]:
        """
        calculate Good Weight List based on good indiv

        Parameters
        ----------
        popX: List[np.ndarray]
            poplation variables list
        popY: List[np.ndarray]
            poplation evaluations list
        goodIndiv: np.ndarray
            Indiv having highest multiobjective acquisition fuction value

        Returns
        -------
        sortedWeightedList: List[Tuple[float, BayesianModelInterface, float, int]]
            weight vector list sorted by EI value
        """
        # 各重みベクトルごとに候補解でのEI値を求めてソート
        obj: int = len(popY[0])
        ws: List[np.ndarray] = UniformalWeight().generateWeightList(obj, 10 * obj)

        sortList: List[Tuple[float, BayesianModelInterface, float, int]] = []
        pbi: ScalarizationInterface = PBI(3.0)
        for i, g in enumerate(ws):
            Y = np.array([pbi.f(y, g) for y in popY])
            model: BayesianModelInterface = GPR(np.array(popX), Y)
            m, v = model.getPredictDistribution(goodIndiv)
            basis = np.min(Y)
            ei = EI().f(m, v, basis)
            sortList.append((ei, model, basis, i))

        sortedWeightedList = list(reversed(sorted(sortList, key=lambda x: x[0])))[:5]
        return sortedWeightedList

    def EfficientGlobalOptimization(
        self,
        model: BayesianModelInterface,
        basis: float,
        DIM: int,
        searchSize: int = 100,
    ) -> Tuple[np.ndarray, float]:
        """
        EfficientGlobalOptimization(EGO) using defined model

        Parameters
        ----------
        model: BayesianModelInterface
            defined model(target problem's model)
        basis: float
            minimum value
        DIM:int
            number of dimensions
        seachSize: int
            number of candidate solution
        """
        newIndiv: np.ndarray
        ei_max: float = -1.0
        for x in RandomSampling().Sampling(searchSize, DIM):
            m, v = model.getPredictDistribution(x)
            ei = EI().f(m, v, basis)
            if ei > ei_max:
                ei_max = ei
                newIndiv = x
        return newIndiv, ei_max

    def EItoEHVI(
        self,
        popX: List[np.ndarray],
        popY: List[np.ndarray],
        indivCandidateListEI: List[Tuple[np.ndarray, float, int]],
    ):
        """
        change EI to EHVI each variables.

        Parameters
        ----------
        popX: List[np.ndarray]
            poplation variables list
        popY: List[np.ndarray]
            poplation evaluations list
        indivCandidateListEI: List[Tuple[np.ndarray, float, int]]
            before indiv list

        Returns
        -------
        indivCandidateListEHVI: List[Tuple[np.ndarray, float, int]]
            after indiv list
        """
        # モデル生成
        models: List[BayesianModelInterface] = [
            GPR(np.array(popX), y) for y in np.transpose(popY)
        ]
        # 各解でEHVI値を計算
        indivCandidateListEHVI: List[Tuple[np.ndarray, float, int]] = []
        for indiv, _, it in indivCandidateListEI:
            mvl: List[Tuple[float, float]] = [
                model.getPredictDistribution(indiv) for model in models
            ]
            ms, vs = np.transpose(mvl)
            ehvi: float = EHVI().f(ms, vs, popY)
            indivCandidateListEHVI.append((indiv, ehvi, it))
        return indivCandidateListEHVI

    def search(
        self, popX: List[np.ndarray], popY: List[np.ndarray]
    ) -> Tuple[np.ndarray, float]:
        """
        seach algorithm.

        Parameters
        ----------
        popX: List[np.ndarray]
            poplation variables list
        popY: List[np.ndarray]
            poplation evaluations list

        Returns
        -------
        newIndiv: np.ndarray
            most good solution's variables
        """

        # 基準解の導出
        goodIndiv: np.ndarray = EHVISearch().search(popX, popY)[0]

        # 優良な重みベクトルの選定
        sortedWeightedList: List[
            Tuple[float, BayesianModelInterface, float, int]
        ] = self.calculateGoodWeightList(popX, popY, goodIndiv)

        # 各優良な重みベクトルでEGO
        indivCandidateListEI: List[Tuple[np.ndarray, float, int]] = [
            self.EfficientGlobalOptimization(model, basis, len(popX[0])) + (i,)
            for _, model, basis, i in sortedWeightedList
        ]

        # 各解でEHVI値を計算し，最も高いEHVI値を持つ解を候補解とする
        indivCandidateListEHVI: List[Tuple[np.ndarray, float, int]] = self.EItoEHVI(
            popX, popY, indivCandidateListEI
        )
        newIndiv, afVal, it = max(indivCandidateListEHVI, key=lambda x: x[1])

        self.__output(len(popY[0]), it)
        return newIndiv, afVal

    def __output(self, obj: int, it: int) -> None:
        ws: List[np.ndarray] = UniformalWeight().generateWeightList(obj, 10 * obj)
        for x in ws[it]:
            print(x, end=",")
        logger.info(ws[it])
