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
        self.__method: SearchInterface = selectSeachAlgorithm(method)
        self.__mEval: int = mEval

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

            # search new individual
            newIndiv: np.ndarray
            af: float
            newIndiv, af = self.__method.search(popX, popY)

            # evaluate and add new individual
            popX.append(newIndiv)
            popY.append(prob.f(newIndiv, obj))
            hv: float = compute_pyhv(popY, [1.0 for _ in range(obj)])

            # output
            print()
            print(hv, af, sep=",", end="\n")
