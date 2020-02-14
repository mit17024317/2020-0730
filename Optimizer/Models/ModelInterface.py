#!/usr/bin/env python3
"""Surrogate Model Interface."""

__author__ = "R.Nakata"
__date__ = "2020/02/06"

from typing import Protocol, Tuple

import numpy as np


class ModelInterface(Protocol):
    """
    Surrogate Model interface
    """

    def __init__(self, sampleX: np.ndarray, sampleY: np.ndarray) -> None:
        """
        Parameters
        ----------
        samplX: np.ndarray<m, d>
            design variables of sample points
        samplY: np.ndarray<m>
            objective variables of sample points
        """
        ...

    def getPredictValue(self, x: np.ndarray) -> float:
        """
        calcrate objective value

        Parameters
        ----------
        x: np.ndarray<d>
            design variables

        Returns
        -------
        y: float
            predect of objective variables
        """
        ...


class BayesianModelInterface(ModelInterface, Protocol):
    """
    Bayesian Surrogate Model interface
    """

    def getPredictDistribution(self, x: np.ndarray) -> Tuple[float, float]:
        """
        calcrate distribution(mean, variance)

        Parameters
        ----------
        x: np.ndarray<d>
            design variables

        Returns
        -------
        (m,v): (float, float)
            mean and variance
        """
        ...
