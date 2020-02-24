#!/usr/bin/env python3
"""WFG Test Problem."""

__author__ = "R.Nakata"
__date__ = "2020/02/24"


import sys
from logging import getLogger

import numpy as np
from optproblems import Individual, wfg

logger = getLogger(__name__)

refP: np.ndarray = np.array([3, 5, 7, 11, 13, 15, 17, 19])


def evaluateWFG(WFG: wfg.WFG, x: np.ndarray, obj: int) -> np.ndarray:
    k: int = 2 * (obj - 1)
    if k >= len(x):
        logger.fatal("#dim must be less than 2*(#obj-1) on WFG problems")
        logger.fatal("--- forced termination ---")
        sys.exit()
    prob: wfg.WFG = WFG(obj, len(x), k)
    indiv: Individual = Individual(x)
    prob.evaluate(indiv)
    val = np.array(indiv.objective_values) / refP[:obj]
    return val


class WFG1:
    def f(self, x: np.ndarray, obj: int) -> np.ndarray:
        val: np.ndarray = evaluateWFG(wfg.WFG1, x, obj)
        return val


class WFG2:
    def f(self, x: np.ndarray, obj: int) -> np.ndarray:
        val: np.ndarray = evaluateWFG(wfg.WFG2, x, obj)
        return val


class WFG3:
    def f(self, x: np.ndarray, obj: int) -> np.ndarray:
        val: np.ndarray = evaluateWFG(wfg.WFG3, x, obj)
        return val


class WFG4:
    def f(self, x: np.ndarray, obj: int) -> np.ndarray:
        val: np.ndarray = evaluateWFG(wfg.WFG4, x, obj)
        return val


class WFG5:
    def f(self, x: np.ndarray, obj: int) -> np.ndarray:
        val: np.ndarray = evaluateWFG(wfg.WFG5, x, obj)
        return val


class WFG6:
    def f(self, x: np.ndarray, obj: int) -> np.ndarray:
        val: np.ndarray = evaluateWFG(wfg.WFG6, x, obj)
        return val


class WFG7:
    def f(self, x: np.ndarray, obj: int) -> np.ndarray:
        val: np.ndarray = evaluateWFG(wfg.WFG7, x, obj)
        return val


class WFG8:
    def f(self, x: np.ndarray, obj: int) -> np.ndarray:
        val: np.ndarray = evaluateWFG(wfg.WFG8, x, obj)
        return val


class WFG9:
    def f(self, x: np.ndarray, obj: int) -> np.ndarray:
        val: np.ndarray = evaluateWFG(wfg.WFG9, x, obj)
        return val
