#!/usr/bin/env python3
"""Scalarization Interface."""

__author__ = "R.Nakata"
__date__ = "2020/02/18"


from typing import List, Protocol

import numpy as np


class ScalarizationInterface(Protocol):
    """
    Scalarization function interface.
    """

    def f(self, x: np.ndarray, w: np.ndarray) -> float:
        """
        Scalarization function.

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
        ...
