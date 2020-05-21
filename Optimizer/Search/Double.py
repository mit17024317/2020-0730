#!/usr/bin/env python3
"""Search algorithm based on EHVI and EI."""

__author__ = "R.Nakata"
__date__ = "2020/05/22"

from logging import getLogger
from typing import List, Tuple

import numpy as np
from mypythontools.Design import Singleton

from .Acquisition.EI import EI
from .AcquisitionSearch import AcquisitionSearchSingle
from .EHVISearch import EHVISearch
from .Scalarization.Tchebycheff import Tchebycheff
from .SearchInterface import SearchInterface

logger = getLogger()


class Double(Singleton):
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
        candidateIndiv: np.ndarray
        candidateIndiv, _ = EHVISearch().search(popX, popY)

        ws: np.ndarray = np.array(
            [x / np.sum(candidateIndiv * candidateIndiv) for x in candidateIndiv]
        )
        logger.debug(candidateIndiv)
        logger.debug(ws)

        searchAlgorithm: SearchInterface = AcquisitionSearchSingle(
            EI(), Tchebycheff(), ws
        )
        return searchAlgorithm.search(popX, popY)
