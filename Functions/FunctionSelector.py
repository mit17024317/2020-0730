#!/usr/bin/env python3
"""Problem select method"""

__author__ = "R.Nakata"
__date__ = "2020/02/04"


from .BenchmarkFunctions import Rastrigin, Rosenbrock, Schwefel
from .FunctionInterface import FunctionInterface
from .TSK import TSK1, TSK2
from .WFG import WFG1, WFG2, WFG3, WFG4, WFG5, WFG6, WFG7, WFG8, WFG9
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
    if name == "TSK1":
        return TSK1()
    if name == "TSK2":
        return TSK2()
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
    if name == "WFG1":
        return WFG1()
    if name == "WFG2":
        return WFG2()
    if name == "WFG3":
        return WFG3()
    if name == "WFG4":
        return WFG4()
    if name == "WFG5":
        return WFG5()
    if name == "WFG6":
        return WFG6()
    if name == "WFG7":
        return WFG7()
    if name == "WFG8":
        return WFG8()
    if name == "WFG9":
        return WFG9()

    assert False, f'Function "{name}" is not defined.'
