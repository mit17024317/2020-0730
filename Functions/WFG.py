#!/usr/bin/env python3
"""WFG Test Problem."""

__author__ = "R.Nakata"
__date__ = "2020/02/24"


import numpy as np
from optproblems import Individual, wfg


def evaluateWFG(WFG: wfg.WFG, x: np.ndarray) -> np.ndarray:
    indiv: Individual = Individual(x)
    WFG.evaluate(indiv)
    val = np.array(indiv.objective_values)
    return val


class WFG1:
    def f(self, x: np.ndarray, obj: int) -> np.ndarray:
        prob: wfg.WFG1 = wfg.WFG1(obj, len(x), 4)
        val: np.ndarray = evaluateWFG(prob, x)
        return val
