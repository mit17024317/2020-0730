#!/usr/bin/env python3
"""Test Function Interface."""

__author__ = "R.Nakata"
__date__ = "2020/02/04"
from typing import Protocol

import numpy as np


class FunctionInterface(Protocol):
    def f(self, x: np.ndarray) -> np.ndarray:
        ...
