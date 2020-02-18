#!/usr/bin/env python3
"""Weight Vector."""

__author__ = "R.Nakata"
__date__ = "2020/02/18"


from typing import List, Protocol

import numpy as np
from numpy.random import rand


class WeightInterface(Protocol):
    """
    Weight Vector interface
    """

    def generateWeightList(self, dim: int, division: int) -> List[np.ndarray]:
        """
        generate Weight vector List

        Parameters
        ----------
        dim: int
            number of design variable
        division: int
            division number of weight
        """
        ...


class RandomWeight:
    """
    Random Weight Vector
    """

    def generateWeightList(self, dim: int, division: int) -> List[np.ndarray]:
        """
        random generate Weight vector List

        Parameters
        ----------
        dim: int
            number of design variable
        division: int
            division number of weight
        """
        weightVectorListSuitable: List[np.ndarray] = [
            np.array([rand() for _ in range(dim)]) for __ in range(division)
        ]
        weightVectorList: List[np.ndarray] = [
            wv / np.sqrt(np.sum(np.frompyfunc(lambda x: x * x, 1, 1)(wv)))
            for wv in weightVectorListSuitable
        ]
        return weightVectorList


class UniformalWeight:
    """
    Uniformal Weight Vector
    """

    def generateWeightList(self, dim: int, division: int) -> List[np.ndarray]:
        """
        generate Uniformal Weight vector List

        Parameters
        ----------
        dim: int
            number of design variable
        division: int
            division number of weight
        """
        self.weightVectorListSuitable: List[np.ndarray] = []
        wv: List[float] = [0.0 for _ in range(dim)]
        self.__dfs(wv, dim, division, 0, 0.0)

        weightVectorList: List[np.ndarray] = [
            wv / np.sqrt(np.sum(np.frompyfunc(lambda x: x * x, 1, 1)(wv)))
            for wv in self.weightVectorListSuitable
        ]
        return weightVectorList

    def __dfs(
        self, wv: List[float], dim: int, division: int, it: int, s: float
    ) -> None:
        """
        generate all weight vector using dfs

        Parametrize
        -----------
        wv: list[float]
            now Weight Vector
        dim: int
            number of design variable
        division: int
            division number of weight
        it: int
            now irerator
        s: float
            now sum
        """
        if it == dim:
            if np.abs(s - 1.0) < 1e-5:
                self.weightVectorListSuitable.append(np.array(wv))
            return

        for p in range(division + 1):
            adder = p / division
            if s + adder > 1.0:
                return
            wv[it] = adder
            self.__dfs(wv, dim, division, it + 1, s + adder)
