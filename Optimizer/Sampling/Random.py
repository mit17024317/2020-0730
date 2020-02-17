#!/usr/bin/env python3
"""Random Sampling."""

__author__ = "R.Nakata"
__date__ = "2020/02/17"

from typing import List

import numpy as np
from numpy.random import rand


class RandomSampling:
    """
    Random Sampling
    """

    def Sampling(self, n: int, d: int) -> List[np.ndarray]:
        """
        initial d dimension sampling #n

        Parameters
        ----------
        n: int
            initial population size
        d: int
            dimension

        Returns
        -------
        pop: List<np.ndarray<float>>
            initial poplation
        """
        pop: List[np.ndarray] = [
            np.array([rand() for _ in range(d)]) for __ in range(n)
        ]
        return pop
