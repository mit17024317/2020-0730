#!/usr/bin/env python3
"""Experiment Result output"""

__author__ = "R.Nakata"
__date__ = "2020/06/12"

from typing import List

import numpy as np
from mypythontools.Design import Singleton

from Optimizer.tools.python_mo_util.pymoutils import compute_pyhv


""" format

// firstOutput
[#design], [#objective]
[design[0]], ..., [design[m]], [objective[0], ...,[objective[n]]
...{sample size}
[design[0]], ..., [design[m]], [objective[0], ...,[objective[n]]

// genOutput
[
    [search algorithm output]
    [hypervolume]
    [design[0]], ..., [design[m]], [objective[0], ...,[objective[n]]
]
...{evaluate size}
[
    [search algorithm output]
    [hypervolume]
    [design[0]], ..., [design[m]], [objective[0], ...,[objective[n]]
]
"""


class OModules(Singleton):
    def firstOutput(self, popX: List[np.ndarray], popY: List[np.ndarray]) -> None:
        """
        first output.

        Parameters
        ----------
        popX: List[np.ndarray]
            poplation variables list
        popY: List[np.ndarray]
            poplation evaluations list
        """
        des: int = len(popX[0])
        obj: int = len(popY[0])
        print(des, obj, sep=",", end="\n")

        for x, y in zip(popX, popY):
            for t in x:
                print(t, end=",")
            for t in y:
                print(t, end=",")
            print()

    def genOutput(self, popX: List[np.ndarray], popY: List[np.ndarray]) -> None:
        """
        output per generation

        Parameters
        ----------
        popX: List[np.ndarray]
            poplation variables list
        popY: List[np.ndarray]
            poplation evaluations list
        """
        obj: int = len(popY[0])

        # search algorithm output end
        print()

        # hypervolume
        hv: float = compute_pyhv(popY, [1.0 for _ in range(obj)])
        print(hv, end="\n")

        # individual information
        for t in popX[-1]:
            print(t, end=",")
        for t in popY[-1]:
            print(t, end=",")
        print()
