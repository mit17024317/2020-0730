#!/usr/bin/env python3
"""Surrogate Assisted Multiobjective Evolutionary Alogorithm"""

__author__ = "R.Nakata"
__date__ = "2020/02/07"


from typing import List

import numpy as np

from Functions.FunctionInterface import FunctionInterface

from .Acquisition.EI import EI
from .Sampling.LHS import LatinHypercubeSampling
from .Sampling.SamplingInterface import SamplingInterface


class SurrogateOptimizer:
    """
    Surrogate Assisted Multiobjective Evolutionary Alogorithm
    """

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
        popY: List[np.ndarray] = [np.array([prob.f(x)]) for x in popX]

        # generate and update
        newIndiv = self.__search()
        popX.append(newIndiv)

        return popY

    def __search(self) -> np.ndarray:
        """
        Search new individual with acqusition function
        """
        # TODO: 後でクラスに切り出す

        # TODO:Interfaceを使う
        af: EI = EI()
        ei = af.f(5.0, 1.0, 3.0)
        print(ei)
        return np.array([1, 1])
