#!/usr/bin/env python3
"""Gaussian Process Regression class"""

__author__ = "R.Nakata"
__date__ = "2020/02/06"

from typing import List, Tuple

import GPy
import numpy as np


class GPR:
    """
    Gaussian Process Regression
    (implement BayesianModelInterface)

    attributes
    ----------
    __model: Gpy.model
        Surrogate Model
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
        DIM: int = len(sampleX[0])
        kernel: GPy.kern = GPy.kern.sde_RBF(DIM) + GPy.kern.Matern32(DIM)
        self.__model: GPy.model = GPy.models.GPRegression(
            sampleX, sampleY[:, None], kernel=kernel
        )
        self.__model.optimize(max_iters=100000)
        self.debug = self.__model

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
        return self.getPredictDistribution(x)[0]

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
        # NOTE:tupleで初期化する場合の変数アノテーションのやり方分からん
        ml: List[List[float]]
        vl: List[List[float]]
        ml, vl = self.__model.predict(np.array([x]))
        m: float = ml[0][0]
        v: float = vl[0][0]
        return m, v
