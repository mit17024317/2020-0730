#!/usr/bin/env python3
"""Search select method"""

__author__ = "R.Nakata"
__date__ = "2020/02/17"

from logging import getLogger

from .Double import Double
from .EHVISearch import EHVISearch
from .parEGO import parEGO
from .Repeat import RepeatAlgorithm
from .SearchInterface import SearchInterface
from .Switch import SwitchAlgorithm

logger = getLogger(__name__)


def selectSeachAlgorithm(name: str, param: dict) -> SearchInterface:
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

    if name == "EHVI":
        return EHVISearch()
    if name == "Repeat":
        return RepeatAlgorithm(param)
    if name == "parEGO":
        return parEGO()
    if name == "Switch":
        return SwitchAlgorithm()
    if name == "Double":
        return Double()

    logger.critical(f'Algotirhm "{name}" is not defined.')
    assert False
