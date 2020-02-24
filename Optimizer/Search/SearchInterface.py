#!/usr/bin/env python3
"""Search algorithm interface."""

__author__ = "R.Nakata"
__date__ = "2020/02/14"


from typing import List, Protocol, Tuple

import numpy as np


class SearchInterface(Protocol):
    """
    Search algorithm interface.
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
        ...
