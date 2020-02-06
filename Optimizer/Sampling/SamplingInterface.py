#!/usr/bin/env python3
"""Sampling Interface."""

__author__ = "R.Nakata"
__date__ = "2020/02/07"

from typing import List, Protocol

import numpy as np


class SamplingInterface(Protocol):
    """
    Sampling interface
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
        ...
