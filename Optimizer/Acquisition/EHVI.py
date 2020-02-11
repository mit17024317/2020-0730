#!/usr/bin/env python3
"""Expected Hypervolume Improvement."""
# TODO:インターフェースにのせる

__author__ = "R.Nakata"
__date__ = "2020/02/12"

from typing import List

import numpy as np


class EHVI:
    """
    Approximation of Expected Hypervolume Improvement.
    """

    def f(self, mean: np.ndarray, var: np.ndarray, pops: List[np.ndarray]) -> float:
        """
        Acquisition function

        Parameters
        ----------
        mean: np.ndarray
            mean
        var: np.ndarray
            variance
        pops: List<np.ndarray>
            all populations

        Returns
        -------
        av: float
            Expected Hypervolume Improvement.
        """
        return 1.0
