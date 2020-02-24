#!/usr/bin/env python3
"""Search algorithm based on Acquisition function."""

__author__ = "R.Nakata"
__date__ = "2020/02/14"


from typing import List

import numpy as np
from numpy.random import rand

from Models.GPR import GPR
from Models.ModelInterface import BayesianModelInterface
from Tools.stop_watch import stop_watch

from ..Sampling.Random import RandomSampling
from .Acquisition.AcquisitionInterface import AcquisitionMultiInterface
from .Acquisition.EHVI import EHVI


class NormalAlgorithm:
    """
    Search algorithm based on Acquisition function.

    attributes
    ----------
    __af: AcquisitionMultiInterface
        Acquisition function for Multiobjective
    """

    def __init__(self, af: AcquisitionMultiInterface = EHVI()) -> None:
        """
        Parameters
        ----------
        af: AcquisitionMultiInterface
            Acquisition function for Multiobjective
        """
        self.__af: AcquisitionMultiInterface = af

    @stop_watch
    def search(self, popX: List[np.ndarray], popY: List[np.ndarray]) -> np.ndarray:
        """
        seach algorithm.

        Parameters
        ----------
        popX: List[np.ndarray]
            poplation variables list
        popY: List[np.ndarray]
            poplation evaluations list

        Returns
        -------
        newIndiv: np.ndarray
            most good solution's variables
        """
        DIM: int = len(popX[0])
        # TODO:CMA-ESの導入
        searchSize: int = 100
        newIndiv: np.ndarray
        ehvi_max: float = -1.0
        r = RandomSampling()
        for x in r.Sampling(searchSize, DIM):
            models: List[BayesianModelInterface] = [
                GPR(np.array(popX), y) for y in np.transpose(popY)
            ]
            ms: List[float] = []
            vs: List[float] = []
            for model in models:
                m, v = model.getPredictDistribution(x)
                ms.append(m)
                vs.append(v)
            ehvi: float = self.__af.f(ms, vs, popY)
            if ehvi > ehvi_max:
                ehvi_max = ehvi
                newIndiv = x
        return newIndiv
