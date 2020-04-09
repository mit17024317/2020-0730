#!/usr/bin/env python3
"""Expected Improvement"""

__author__ = "R.Nakata"
__date__ = "2020/02/07"

from typing import Protocol

import numpy as np
from mypythontools.Design import Singleton
from scipy.stats import norm


class EI(Singleton):
    """
    Expected Improvement
    """

    def f(self, mean: float, var: float, basis: float) -> float:
        """
        Acquisition function

        Parameters
        ----------
        mean: float
            mean
        var: float
            variance
        basis: float
            basis value

        Returns
        -------
        av: float
            acquisition value
        """
        s: float = np.sqrt(var)
        nm: float = (basis - mean) / s
        return nm * s * norm.cdf(nm, 0, 1) + s * norm.pdf(nm, 0, 1)
