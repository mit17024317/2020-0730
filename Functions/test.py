#!/usr/bin/env python3
"""Linear Basis Function Model."""

__author__ = "R.Nakata"
__date__ = "2019/11/01"

from abc import ABC, abstractmethod
from logging import DEBUG, basicConfig, getLogger

logger = getLogger(__name__)
basicConfig(level=DEBUG)


class A:
    def __init__(self):
        pass


def f(x: int) -> int:
    return 1
