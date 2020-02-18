#!/usr/bin/env python3
"""Penalty Boundary Intersection."""

__author__ = "R.Nakata"
__date__ = "2020/02/18"


from typing import List, Protocol

import numpy as np


class PBI:
    """
    Penalty Boundary Intersection.

    attributes
    ----------
    __theta: float
        hyper Parameter
    """

    def __init__(self, theta: float) -> None:
        """
        Parameters
        ----------
        theta: float
            hyper Parameter
        """
        self.__theta = theta

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
        d1: float = np.dot(x, w)
        d2: float = np.linalg.norm(x - d1 * w)
        value: float = d1 + self.__theta * d2
        return value
