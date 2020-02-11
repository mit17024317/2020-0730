#!/usr/bin/env python3
"""Surrogate Assisted Multiobjective Evolutionary Alogorithm"""

__author__ = "R.Nakata"
__date__ = "2020/02/07"


from typing import List, Tuple

import numpy as np
from numpy.random import rand

from Functions.FunctionInterface import FunctionInterface
from Models.GPR import GPR
from Models.ModelInterface import BayesianModelInterface

from .Acquisition.EHVI import EHVI
from .Acquisition.EI import EI
from .Sampling.LHS import LatinHypercubeSampling
from .Sampling.SamplingInterface import SamplingInterface


class SurrogateOptimizer:
    """
    Surrogate Assisted Multiobjective Evolutionary Alogorithm
    """

    # TODO: Modelを受け取る
    def __init__(self) -> None:
        ...

    def optimize(
        self,
        prob: FunctionInterface,
        obj: int,
        dim: int,
        initializer: SamplingInterface = LatinHypercubeSampling(),
    ) -> List[np.ndarray]:

        # Initialize
        popX: List[np.ndarray] = initializer.Sampling(5, dim)
        popY: List[np.ndarray] = [np.array(prob.f(x)) for x in popX]

        # generate and update
        for _ in range(30):
            newIndiv: np.ndarray = self.__search(popX, popY)
            popX.append(newIndiv)
            popY.append(prob.f(newIndiv))

        return popY

    def __search(
        self, popX: List[np.ndarray], popY: List[np.ndarray], key: str = "original"
    ) -> np.ndarray:
        """
        Search new individual with acqusition function
        """
        # TODO: 後でクラスに切り出す
        if key == "EHVI":
            return self.___EHVI(popX, popY)
        if key == "original":
            return self.___original(popX, popY)
        else:
            assert False, "早くインターフェスを作る！"

    def __generageModel(
        self, popX: List[np.ndarray], popY: List[np.ndarray]
    ) -> List[BayesianModelInterface]:

        X = np.array(popX)
        Y = np.transpose(popY)
        models: List[BayesianModelInterface] = [GPR(X, y) for y in Y]
        return models

    # TODO:ここ以下をなんとかする
    """
    以下は全て実験用のゴミコードである
    """

    def ___EHVI(self, popX: List[np.ndarray], popY: List[np.ndarray]) -> np.ndarray:
        DIM: int = len(popX[0])
        # TODO:Interfaceを使う
        afm: EHVI = EHVI()
        # TODO:CMA-ESの導入
        searchSize: int = 1
        newIndiv: np.ndarray
        ehvi_max: float = -1.0
        for x in [np.array([rand() for _ in range(DIM)]) for __ in range(searchSize)]:
            models: List[BayesianModelInterface] = self.__generageModel(
                popX, popY)
            ms: List[float] = []
            vs: List[float] = []
            for model in models:
                m, v = model.getPredictDistribution(x)
                ms.append(m)
                vs.append(v)
            ehvi: float = afm.f(ms, vs, popY)
            if ehvi > ehvi_max:
                ehvi_max = ehvi
                newIndiv = x
        return newIndiv

    def ___original(self, popX: List[np.ndarray], popY: List[np.ndarray]) -> np.ndarray:
        DIM: int = len(popX[0])

        # 候補の導出
        goodIndiv: np.ndarray = self.___EHVI(popX, popY)

        # 各重みベクトルごとに候補解でのEI値を求めてソート
        af = EI()
        obj: int = len(popY[0])
        gn: int = 10
        gs: List[List[float]] = [[rand() for _ in range(obj)]
                                 for __ in range(gn)]
        sortList: List[Tuple[float, BayesianModelInterface, float]] = []
        for i, g in enumerate(gs):
            Y = np.array([np.sum(np.array(g) * y) for y in popY])
            model: BayesianModelInterface = GPR(np.array(popX), Y)
            m, v = model.getPredictDistribution(goodIndiv)
            basis = np.min(Y)
            ei = af.f(m, v, basis)
            sortList.append((ei, model, basis))
        sortList = reversed(sorted(sortList, key=lambda x: x[0]))

        # EI値による探索
        searchSize: int = 1
        newIndiv: np.ndarray
        ei_max: float = -1.0
        for _, model, basis in list(sortList)[:5]:
            for x in [
                np.array([rand() for _ in range(DIM)]) for __ in range(searchSize)
            ]:
                m, v = model.getPredictDistribution(x)
                ei = af.f(m, v, basis)
                if ei > ei_max:
                    ei_max = ei
                    newIndiv = x
        return newIndiv
