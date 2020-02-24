#!/usr/bin/env python3
"""Gaussian Process Regression class"""

__author__ = "R.Nakata"
__date__ = "2020/02/06"

import logging
import warnings
from typing import List, Tuple

import GPy
import numpy as np

logger = logging.getLogger(__name__)


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
        samplX: np.ndarray<np.ndarray<float>>
            design variables of sample points
        samplY: np.ndarray<float>
            objective variables of sample points
        """
        # disable logger output and warnings
        with self.__DisableRunnningInfomation():
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
        x: np.ndarray<float>
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
        x: np.ndarray<float>
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
        # 計算誤差による分散のマイナス値を補正
        v = 0.0 if v < 0.0 else v
        return m, v

    def getPredictDistributionAll(self, xList: np.ndarray) -> np.ndarray:
        """
        calcrate distribution(mean, variance) on all x

        Parameters
        ----------
        xList: np.ndarray<np.ndarray<float>>
            all design variables

        Returns
        -------
        y: np.ndarray<Tuple<float,float>>
            all mean and variance
        """
        mvListTrans: Tuple[np.ndarray, np.ndarray] = self.__model.predict(xList)
        mvList: np.ndarray = np.transpose(mvListTrans)[0]
        # 計算誤差による分散のマイナス値を補正
        for mv in mvList:
            mv[1] = 0.0 if mv[1] < 0.0 else mv[1]

        return mvList

    class __DisableRunnningInfomation:
        """
        disable logging and warnings, use as below
        with __DisableRunnningInfomation():
            do_something()
        """

        def __enter__(self):
            logging.disable(logging.INFO)
            warnings.simplefilter("ignore")

        def __exit__(self, _, __, ___):
            logging.disable(logging.NOTSET)
            warnings.resetwarnings()
