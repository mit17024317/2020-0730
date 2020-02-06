#!/usr/bin/env python3
"""Expected Improvement"""

__author__ = "R.Nakata"
__date__ = "2020/02/07"

from typing import Protocol

import numpy as np


class EI:
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
        ...
