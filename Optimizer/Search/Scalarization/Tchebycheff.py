#!/usr/bin/env python3
"""Tchbycheff function."""

__author__ = "R.Nakata"
__date__ = "2020/02/18"


from typing import List, Protocol

import numpy as np
from mypythontools.Design import Singleton


class Tchebycheff(Singleton):
    """
    Tchbychef function.
    """

    def f(self, x: np.ndarray, w: np.ndarray) -> float:
        """
        Scalarization function.
        reference point is (0.0,...,0.0)

        Parameters
        ----------
        x: np.ndarray
            deign variables
        w: np.ndarray
            weight vector

        Returns
        -------
        value: float
            scalar value
        """
        value: float = np.max(x * w)
        return value
