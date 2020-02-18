#!/usr/bin/env python3
"""multi acquisition Search algorithm."""

__author__ = "R.Nakata"
__date__ = "2020/02/14"


from typing import List, Tuple

import numpy as np
from Models.GPR import GPR
from Models.ModelInterface import BayesianModelInterface

from ..Sampling.Random import RandomSampling
from .Acquisition.EI import EI
from .Normal import NormalAlgorithm
from .Scalarization.PBI import PBI
from .Scalarization.ScalarizationInterface import ScalarizationInterface
from .Scalarization.WeightVector import RandomWeight
from .SearchInterface import SearchInterface


class RepeatAlgorithm:
    """
    multi acquisition Search algorithm.
    """

    def search(self, popX: List[np.ndarray], popY: List[np.ndarray]) -> np.ndarray:
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
        DIM: int = len(popX[0])

        # 候補の導出
        multiAlg: SearchInterface = NormalAlgorithm()
        goodIndiv: np.ndarray = multiAlg.search(popX, popY)

        # 各重みベクトルごとに候補解でのEI値を求めてソート
        af = EI()
        obj: int = len(popY[0])
        ws: List[np.ndarray] = RandomWeight().generateWeightList(obj, 100)

        sortList: List[Tuple[float, BayesianModelInterface, float]] = []
        pbi: ScalarizationInterface = PBI(3.0)
        for i, g in enumerate(ws):
            Y = np.array([pbi.f(y, g) for y in popY])
            model: BayesianModelInterface = GPR(np.array(popX), Y)
            m, v = model.getPredictDistribution(goodIndiv)
            basis = np.min(Y)
            ei = af.f(m, v, basis)
            sortList.append((ei, model, basis))
        sortList = reversed(sorted(sortList, key=lambda x: x[0]))

        # EI値による探索
        searchSize: int = 100
        newIndiv: np.ndarray
        ei_max: float = -1.0
        for _, model, basis in list(sortList)[:5]:
            r = RandomSampling()
            for x in r.Sampling(searchSize, DIM):
                m, v = model.getPredictDistribution(x)
                ei = af.f(m, v, basis)
                if ei > ei_max:
                    ei_max = ei
                    newIndiv = x
        return newIndiv
