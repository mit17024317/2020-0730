#!/usr/bin/env python3
"""Surrogate Assisted Multiobjective Evolutionary Alogorithm"""

__author__ = "R.Nakata"
__date__ = "2020/02/07"

from logging import DEBUG, basicConfig, getLogger
from typing import List

import numpy as np

from Functions.FunctionInterface import FunctionInterface
from Optimizer.tools.python_mo_util.pymoutils import compute_pyhv

from .Sampling.LHS import LatinHypercubeSampling
from .Sampling.SamplingInterface import SamplingInterface
from .Search.SearchInterface import SearchInterface
from .Search.SearchSelector import selectSeachAlgorithm

logger = getLogger(__name__)


class SurrogateOptimizer:
    """
    Surrogate Assisted Multiobjective Evolutionary Alogorithm
    """

    def __init__(self, method: str) -> None:
        self.method = method

    def optimize(
        self,
        trial: int,
        prob: FunctionInterface,
        obj: int,
        dim: int,
        initialNum: int = 5,
        generations: int = 30,
        initializer: SamplingInterface = LatinHypercubeSampling(),
    ) -> List[np.ndarray]:

        # Initialize
        popX: List[np.ndarray] = initializer.Sampling(initialNum, dim)
        popY: List[np.ndarray] = [np.array(prob.f(x)) for x in popX]

        # generate and update
        for _ in range(generations):
            logger.info(f"{_}世代")
            newIndiv: np.ndarray = self.__search(popX, popY)
            popX.append(newIndiv)
            popY.append(prob.f(newIndiv))
            ip = [1.0 for _ in range(2)]
            # TODO:評価用クラスに委託する
            hv: float = compute_pyhv(popY, ip)
            print(hv)

        return popY

    def __search(self, popX: List[np.ndarray], popY: List[np.ndarray]) -> np.ndarray:
        """
        Search new individual with acqusition function
        """
        s: SearchInterface = selectSeachAlgorithm(self.method)
        return s.search(popX, popY)
