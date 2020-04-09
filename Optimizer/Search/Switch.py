#!/usr/bin/env python3
"""Adapted search"""

__author__ = "R.Nakata"
__date__ = "2020/02/25"


from logging import getLogger
from typing import List, Tuple

import numpy as np

from Optimizer.tools.python_mo_util.pymoutils import compute_pyhv

from .EHVISearch import EHVISearch
from .Repeat import RepeatAlgorithm
from .SearchInterface import SearchInterface

logger = getLogger(__name__)


class SwitchAlgorithm:
    """
    Adapted search algorithm

    attributes
    ----------
    __befAF: float
        The Previous difference between acuisition fuction value and true value
    """

    def __init__(self) -> None:
        self.__befAF: float = 0.0
        self.__nowKey: bool = True

    def __output(self) -> None:
        print(1 if self.__nowKey else 0, end=",")

    def __select(self, popY) -> SearchInterface:
        """
        update algorithm key and select algorithm

        Parameters
        ----------
        popY: List[np.ndarray]
            poplation evaluations list

        Returns
        -------
        Search alogorithm class: SearchInterface
            Search alogorithm
        """
        dif: float
        if self.__befAF > 1e-5:
            logger.warning("adapt")
            if self.__nowKey:
                y0: float = np.min(popY[:-1])
                y1: float = np.min(popY)
                dif = (y0 - y1) - self.__befAF
            else:
                hv0: float = compute_pyhv(popY[:-1], [1.0 for _ in range(len(popY[0]))])
                hv1: float = compute_pyhv(popY, [1.0 for _ in range(len(popY[0]))])
                dif = (hv1 - hv0) - self.__befAF
            if dif < 1e-5:
                self.__nowKey = not self.__nowKey
                self.__befAF = 0.0
        return RepeatAlgorithm() if self.__nowKey else EHVISearch()

        ...

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
        alg: SearchInterface = self.__select(popY)
        newIndiv, af = alg.search(popX, popY)
        self.__befAF = af
        self.__output()
        return newIndiv, af
