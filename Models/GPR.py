#!/usr/bin/env python3
"""Gaussian Process Regression class"""

__author__ = "R.Nakata"
__date__ = "2020/02/06"

import numpy as np


class GPR:
    """
    Gaussian Process Regression
    (implement BayesianModelInterface)
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

    def getPredictDistribution(self, x: np.ndarray) -> float:  # TODO:型を調べて明記する
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
