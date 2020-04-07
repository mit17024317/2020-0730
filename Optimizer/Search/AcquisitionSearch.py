#!/usr/bin/env python3
"""Acquisition function based Search Algorithm."""

__author__ = "R.Nakata"
__date__ = "2020/04/07"


from typing import List, Tuple

import numpy as np
from numpy.random import rand

from Models.GPR import GPR
from Models.ModelInterface import BayesianModelInterface

# TODO: 探索にCMA-ESを導入
from ..Sampling.Random import RandomSampling
from .Acquisition.AcquisitionInterface import (AcquisitionMultiInterface,
                                               AcquisitionSingleInterface)
from .Scalarization.ScalarizationInterface import ScalarizationInterface


class AcquisitionSearchMulti:
    """
    Multi Acquisition function based Search Algorithm..

    attributes
    ----------
    __af: AcquisitionMultiInterface
        Acquisition function for Multiobjective
    """

    def __init__(self, af: AcquisitionMultiInterface) -> None:
        """
        Parameters
        ----------
        af: AcquisitionMultiInterface
            Acquisition function for Multiobjective
        """
        self.__af: AcquisitionMultiInterface = af

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

        # モデル生成
        models: List[BayesianModelInterface] = [
            GPR(np.array(popX), y) for y in np.transpose(popY)
        ]

        # ランダム探索のための探索解を生成
        DIM: int = len(popX[0])
        searchSize: int = 100
        searchPop: List[np.ndarray] = RandomSampling().Sampling(searchSize, DIM)

        # 各解の獲得関数値を計算
        mvl: List[np.ndarray] = [
            model.getPredictDistributionAll(np.array(searchPop)).T for model in models
        ]
        afValList: List[float] = [
            self.__af.f(means, varis, popY) for means, varis in np.transpose(mvl)
        ]

        # 最も良い獲得関数値を持つ解とその値を取得して返す
        afVal: float
        newIndiv: np.ndarray
        newIndiv, afVal = max(zip(searchPop, afValList), key=lambda x: x[1])
        return newIndiv, afVal


class AcquisitionSearchSingle:
    """
    Single Acquisition function based Search Algorithm..

    attributes
    ----------
    __af: AcquisitionSingleInterface
        Acquisition function for Singleobjective
    __sf: ScalarizationInterface
        Scalarization function 
    __weightVector: np.ndarray
        weight vector
    """

    def __init__(
        self,
        af: AcquisitionSingleInterface,
        sf: ScalarizationInterface,
        weightVector: np.ndarray,
    ) -> None:
        """
        Parameters
        ----------
        af: AcquisitionSingleInterface
            Acquisition function for Singleobjective
        sf: ScalarizationInterface
            Scalarization function 
        weightVector: np.ndarray
            weight vector
        """
        self.__af: AcquisitionSingleInterface = af
        self.__sf: ScalarizationInterface = sf
        self.__weightVector: np.ndarray = weightVector

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

        Y = np.array([self.__sf.f(y, self.__weightVector) for y in popY])
        model: BayesianModelInterface = GPR(np.array(popX), Y)

        basis: float = np.min(Y)
        searchSize: int = 5000
        afVal_max: float = -1.0
        DIM: int = len(popX[0])
        for x in RandomSampling().Sampling(searchSize, DIM):
            m, v = model.getPredictDistribution(x)
            afVal: float = self.__af.f(m, v, basis)
            if afVal > afVal_max:
                afVal_max = afVal
                newIndiv = x

        return newIndiv, afVal_max
