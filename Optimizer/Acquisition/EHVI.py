#!/usr/bin/env python3
"""Expected Hypervolume Improvement."""
# TODO:インターフェースにのせる

__author__ = "R.Nakata"
__date__ = "2020/02/12"

from typing import List

import numpy as np
from numpy.random import normal


class EHVI:
    """
    Approximation of Expected Hypervolume Improvement.
    """

    def f(self, mean: List[float], var: List[float], pops: List[np.ndarray]) -> float:
        """
        Acquisition function

        Parameters
        ----------
        mean: List[float] 
            mean
        var: List[float]
            variance
        pops: List<np.ndarray>
            all populations

        Returns
        -------
        av: float
            Expected Hypervolume Improvement.
        """
        from tools.python_mo_util.pymoutils import compute_pyhv

        DIM: int = len(mean)
        ip: np.ndarray = np.array([1.0 for _ in range(DIM)])

        # モンテカルロ積分
        hv: float = compute_pyhv(pops, ip)
        hv_sum: float = 0.0
        size: int = 10000
        for x in [
            np.array([normal(m, v) for m, v in zip(mean, var)]) for _ in range(size)
        ]:
            pops.append(x)
            hv_sum += np.max([compute_pyhv(pops, ip) - hv, 0.0])
            pops.pop()
        ehvi = hv_sum / size

        return ehvi
