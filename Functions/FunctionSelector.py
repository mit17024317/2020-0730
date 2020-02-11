#!/usr/bin/env python3
"""Problem select method"""

__author__ = "R.Nakata"
__date__ = "2020/02/04"


from .BenchmarkFunctions import Rastrigin, Rosenbrock, Schwefel
from .FunctionInterface import FunctionInterface
from .ZDT import ZDT4, ZDT6


def selectFunction(name: str) -> FunctionInterface:
    """
    select function at using name

    Parameters
    ----------
    name: str
        function name

    Returns
    -------
    Function class: FunctionInterface
        Function class corresponding to the name
    """

    if name == "Rastrigin":
        return Rastrigin()
    if name == "Rosenbrock":
        return Rosenbrock()
    if name == "Schwefel":
        return Schwefel()
    if name == "ZDT4":
        return ZDT4()
    if name == "ZDT6":
        return ZDT6()

    assert False, f'Function "{name}" is not defined.'
