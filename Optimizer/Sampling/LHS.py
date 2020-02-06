#!/usr/bin/env python3
"""Sampling Interface."""

__author__ = "R.Nakata"
__date__ = "2020/02/07"

from typing import List, Protocol

import numpy as np
from pyDOE import lhs


class LatinHypercubeSampling:
    """
    Latin Hypercube Sampling
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
        sample: np.ndarray = lhs(d, n)
        pop: List[np.ndarray] = [np.array(s) for s in sample]
        return pop
