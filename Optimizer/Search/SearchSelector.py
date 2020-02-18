#!/usr/bin/env python3
"""Search select method"""

__author__ = "R.Nakata"
__date__ = "2020/02/17"


from .Normal import NormalAlgorithm
from .Repeat import RepeatAlgorithm
from .SearchInterface import SearchInterface


def selectSeachAlgorithm(name: str) -> SearchInterface:
    """
    select Search Interface at using name

    Parameters
    ----------
    name: str
        function name

    Returns
    -------
    Search alogorithm class: SearchInterface 
        Search alogorithm classcorresponding to the name
    """

    if name == "Normal":
        return NormalAlgorithm()
    if name == "Repeat":
        return RepeatAlgorithm()

    assert False, f'Algotirhm "{name}" is not defined.'
