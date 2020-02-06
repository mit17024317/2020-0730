#!/usr/bin/env python3
"""Surrogate Assisted Multiobjective Evolutionary Alogorithm"""

__author__ = "R.Nakata"
__date__ = "2020/02/07"


from typing import List

import numpy as np

from Functions.FunctionInterface import FunctionInterface

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

        pop: List[np.ndarray] = initializer.Sampling(5, dim)
        return pop
