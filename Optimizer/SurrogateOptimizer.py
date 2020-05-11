#!/usr/bin/env python3
"""Surrogate Assisted Multiobjective Evolutionary Alogorithm"""

__author__ = "R.Nakata"
__date__ = "2020/02/07"

from logging import DEBUG, basicConfig, getLogger
from typing import List, Tuple

import numpy as np
from mypythontools.Design import Singleton

from Functions.FunctionInterface import FunctionInterface
from Optimizer.tools.python_mo_util.pymoutils import compute_pyhv

from .Sampling.LHS import LatinHypercubeSampling
from .Sampling.SamplingInterface import SamplingInterface
from .Search.SearchInterface import SearchInterface
from .Search.SearchSelector import selectSeachAlgorithm

logger = getLogger(__name__)


class SurrogateOptimizer(Singleton):
    """
    Surrogate Assisted Multiobjective Evolutionary Alogorithm
    """

    def optimize(
        self,
        prob: FunctionInterface,
        method: str,
        obj: int,
        dim: int,
        methodParam: dict,
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
        method: str
            Optimizer's method name
        obj: int
            number of objective
        dim: int
            number ob design variables
        methodParam: dict
            parameter of select method
        initialNum: int
            Initial popolation size
        generations: int
            number of generations
        initializer: SamplingInterface
            method of Initial Sampling
        """

        optMethod: SearchInterface = selectSeachAlgorithm(method, methodParam)

        # Initialize
        popX: List[np.ndarray] = initializer.Sampling(initialNum, dim)
        popY: List[np.ndarray] = [np.array(prob.f(x, obj)) for x in popX]
        for x in popX:
            for t in x:
                print(t, end=",")
            print()

        # generate and update
        for _ in range(generations):
            logger.info(f"{_} generation")

            # search new individual
            newIndiv: np.ndarray
            af: float
            newIndiv, af = optMethod.search(popX, popY)

            # evaluate and add new individual
            popX.append(newIndiv)
            popY.append(prob.f(newIndiv, obj))
            hv: float = compute_pyhv(popY, [1.0 for _ in range(obj)])

            # output
            print()
            for t in newIndiv:
                print(t, end=",")
            print()
            print(hv, af, sep=",", end="\n")
