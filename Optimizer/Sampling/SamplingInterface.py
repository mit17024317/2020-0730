#!/usr/bin/env python3
"""Sampling Interface."""

__author__ = "R.Nakata"
__date__ = "2020/02/07"

from typing import Protocol

import numpy as np


class SamplingInterface(Protocol):
    """
    Sampling interface
    """

    def Sampling(self, n: int) -> np.ndarray:
        """
        initial sampling #n 

        Parameters
        ----------
        n: int
            initial population size

        Returns
        -------
        pop: np.ndarray<np.ndarray<float>>
            initial poplation
        """
        ...
