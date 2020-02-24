#!/usr/bin/env python3
"""Surrogate Assisted Multiobjective Evolutionary Alogorithm"""

__author__ = "R.Nakata"
__date__ = "2020/02/07"

from logging import DEBUG, basicConfig, getLogger
from typing import List, Tuple

import numpy as np

from Functions.FunctionInterface import FunctionInterface
from Optimizer.tools.python_mo_util.pymoutils import compute_pyhv

from .Sampling.LHS import LatinHypercubeSampling
from .Sampling.SamplingInterface import SamplingInterface
from .Search.Acquisition.EHVI import EHVI
from .Search.SearchInterface import SearchInterface
from .Search.SearchSelector import selectSeachAlgorithm

logger = getLogger(__name__)


class SurrogateOptimizer:
    """
    Surrogate Assisted Multiobjective Evolutionary Alogorithm

    attributes
    ----------
    __method: str
        Optimizer's method name

    """

    def __init__(self, method: str, mEval: int = 1000) -> None:
        """
        Parameters
        ----------
        method: str
            Optimizer's method name
        mEval: int
            evaluation num on surrogate model
        """
        self.__method = method
        self.__mEval = mEval

    def optimize(
        self,
        prob: FunctionInterface,
        obj: int,
        dim: int,
        initialNum: int = 5,
        generations: int = 30,
        initializer: SamplingInterface = LatinHypercubeSampling(),
    ) -> None:
        """
        optimize main method

        Parameters
        ----------
        prob: FunctionInterface
            target problem
        obj: int
            number of objective
        dim: int
            number ob design variables
        initialNum: int
            Initial popolation size
        generations: int
            number of generations
        initializer: SamplingInterface
            method of Initial Sampling
        """
        # TODO: 返り値について考える

        # Initialize
        popX: List[np.ndarray] = initializer.Sampling(initialNum, dim)
        popY: List[np.ndarray] = [np.array(prob.f(x, obj)) for x in popX]

        # generate and update
        for _ in range(generations):
            logger.info(f"{_} generation")

            newIndiv: np.ndarray
            af: float
            newIndiv, af = self.__search(popX, popY)

            popX.append(newIndiv)
            popY.append(prob.f(newIndiv, obj))
            hv: float = compute_pyhv(popY, [1.0 for _ in range(obj)])
            print(hv, af)

    def __search(
        self, popX: List[np.ndarray], popY: List[np.ndarray]
    ) -> Tuple[np.ndarray, float]:
        """
        Search new individual with acqusition function

        Parameters
        ----------
        popX: List[np.ndarray]
            popolation(design variables)
        popY: List[np.ndarray]
            popolation(objective variables)

        Returns
        -------
        newIndiv: np.ndarray
            new individual
        """
        s: SearchInterface = selectSeachAlgorithm(self.__method)
        return s.search(popX, popY)
