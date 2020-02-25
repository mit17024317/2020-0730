#!/usr/bin/env python3
"""Adapted search"""

__author__ = "R.Nakata"
__date__ = "2020/02/25"


from logging import getLogger
from typing import List, Tuple

import numpy as np

from .parEGO import parEGO
from .SearchInterface import SearchInterface

logger = getLogger(__name__)


class Switch:
    """
    Adapted search algorithm

    attributes
    ----------
    __befAF: float
        The Previous difference between acuisition fuction value and true value
    """

    def __init__(self) -> None:
        self.__defAF = 0.0

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
        logger.debug("in")
        p: SearchInterface = parEGO()
        newIndiv, af = p.search(popX, popY)
        return p.search(popX, popY)
