#!/usr/bin/env python3
"""Search algorithm based on Acquisition function."""

__author__ = "R.Nakata"
__date__ = "2020/02/14"

from logging import getLogger
from typing import List

import numpy as np
from numpy.random import rand

from Models.GPR import GPR
from Models.ModelInterface import BayesianModelInterface

from ..Sampling.Random import RandomSampling
from .Acquisition.AcquisitionInterface import AcquisitionMultiInterface
from .Acquisition.EHVI import EHVI

logger = getLogger(__name__)


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
        # TODO:CMA-ESの導入
        models: List[BayesianModelInterface] = [
            GPR(np.array(popX), y) for y in np.transpose(popY)
        ]

        DIM: int = len(popX[0])
        searchSize: int = 100
        searchPop: List[np.ndarray] = RandomSampling().Sampling(searchSize, DIM)

        mvl: List[np.ndarray] = [
            model.getPredictDistributionAll(np.array(searchPop)).T for model in models
        ]
        ehviList: List[float] = [
            self.__af.f(means, varis, popY) for means, varis in np.transpose(mvl)
        ]
        newIndiv: np.ndarray = max(zip(ehviList, searchPop), key=lambda x: x[0])[1]
        return newIndiv
