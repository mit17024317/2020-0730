#!/usr/bin/env python3
"""Acquisition function interface."""
"""
いい感じのインターフェースを考えられなかったので，
本クラスは現状未使用である(2020/02/12)
"""
__author__ = "R.Nakata"
__date__ = "2020/02/07"


from typing import Protocol

import numpy as np


class AcquisitionSingleInterface(Protocol):
    """
    Acquisition function of single-objective interface
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


class AcquisitionMultiInterface(Protocol):
    """
    Acquisition function of multi-objective interface
    """

    def f(self, mean: np.ndarray, var: np.ndarray, basis: float) -> float:
        """
        Acquisition function

        Parameters
        ----------
        mean: np.ndarray
            mean
        var: np.ndarray
            variance
        basis: float
            basis value

        Returns
        -------
        av: float
            acquisition value
        """
        ...
