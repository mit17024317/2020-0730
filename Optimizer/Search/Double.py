#!/usr/bin/env python3
"""Search algorithm based on EHVI and EI."""

__author__ = "R.Nakata"
__date__ = "2020/05/22"

from logging import getLogger
from typing import List, Tuple

import numpy as np
from mypythontools.Design import Singleton

# TODO: searchクラスのインタフェース変更により..Modelを削除
from ..Models.GPR import GPR
from ..Models.ModelInterface import BayesianModelInterface
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

        # TODO:seatchの返り値として推測値を得るようにする
        models: List[BayesianModelInterface] = [
            GPR(np.array(popX), y) for y in np.transpose(popY)
        ]
        ws: np.ndarray = np.array(
            [model.getPredictValue(candidateIndiv) for model in models]
        )
        wsNorm: np.ndarray = np.array([x / np.sqrt(np.sum(ws * ws)) for x in ws])

        searchAlgorithm: SearchInterface = AcquisitionSearchSingle(
            EI(), Tchebycheff(), wsNorm
        )
        newIndiv: np.ndarray
        af: float
        newIndiv, af = searchAlgorithm.search(popX, popY)
        self.__output(models, newIndiv)
        return newIndiv, af

    def __output(self, models, newIndiv):
        val = [m.getPredictValue(newIndiv) for m in models]
        for x in val:
            print(x, end=",")
