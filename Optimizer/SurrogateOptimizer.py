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
        trial: int,
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
        trial: int
            number of trial
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

        # n trial
        for __ in range(trial):
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
                hv: float = compute_pyhv(popY, ip)
                print(hv)

    def __search(self, popX: List[np.ndarray], popY: List[np.ndarray]) -> np.ndarray:
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
