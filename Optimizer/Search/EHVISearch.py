#!/usr/bin/env python3
"""Search algorithm based on EHVI."""

__author__ = "R.Nakata"
__date__ = "2020/04/07"

from typing import List, Tuple

import numpy as np
from mypythontools.Design import Singleton

from ..Models.GPR import GPR
from .Acquisition.EHVI import EHVI
from .AcquisitionSearch import AcquisitionSearchMulti
from .SearchInterface import SearchInterface


class EHVISearch(Singleton):
    """
    Search algorithm based on Acquisition function.
    """

    def search(
        self, popX: List[np.ndarray], popY: List[np.ndarray]
    ) -> Tuple[np.ndarray, float]:
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
        searchAlgorithm: SearchInterface = AcquisitionSearchMulti(EHVI())

        newIndiv: np.ndarray
        af: float
        newIndiv, af = searchAlgorithm.search(popX, popY)
        self.__output(popX, popY, newIndiv)
        return newIndiv, af

    def __output(self, popX, popY, newIndiv):
        # TODO:seatchの返り値として推測値を得るようにする
        models = [GPR(np.array(popX), y) for y in np.transpose(popY)]
        val = [m.getPredictValue(newIndiv) for m in models]
        for x in val:
            print(x, end=",")
