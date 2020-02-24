#!/usr/bin/env python3
"""parEGO(pareto EGO)."""

__author__ = "R.Nakata"
__date__ = "2020/02/18"


from typing import List, Tuple

import numpy as np

from Models.GPR import GPR
from Models.ModelInterface import BayesianModelInterface

from ..Sampling.Random import RandomSampling
from .Acquisition.AcquisitionInterface import AcquisitionMultiInterface
from .Acquisition.EI import EI
from .Scalarization.ScalarizationInterface import ScalarizationInterface
from .Scalarization.Tchebycheff import Tchebycheff
from .Scalarization.WeightVector import RandomWeight


class parEGO:
    """
    parEGO(pareto EGO).
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
        DIM: int = len(popX[0])
        OBJ: int = len(popY[0])
        ws: np.ndarray = RandomWeight().generateWeightList(OBJ, 1)[0]

        tc: ScalarizationInterface = Tchebycheff()
        Y = np.array([tc.f(y, ws) for y in popY])
        model: BayesianModelInterface = GPR(np.array(popX), Y)

        basis: float = np.min(Y)
        af: EI = EI()
        searchSize: int = 5000
        ei_max: float = -1.0
        for x in RandomSampling().Sampling(searchSize, DIM):
            m, v = model.getPredictDistribution(x)
            ei: float = af.f(m, v, basis)
            if ei > ei_max:
                ei_max = ei
                newIndiv = x
        return newIndiv, ei_max
