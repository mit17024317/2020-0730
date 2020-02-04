#!/usr/bin/env python3
"""Problem select method"""

__author__ = "R.Nakata"
__date__ = "2020/02/04"


from .BenchmarkFunctions import Rastrigin, Rosenbrock, Schwefel
from .FunctionInterface import FunctionInterface


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

    assert False, f'Function "{name}" is not defined.'
