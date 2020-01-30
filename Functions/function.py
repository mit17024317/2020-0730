#!/usr/bin/env python3
"""Linear Basis Function Model."""

__author__ = "R.Nakata"
__date__ = "2019/11/01"
from abc import ABC, abstractmethod
from logging import DEBUG, basicConfig, getLogger

import numpy as np

from .test import f

logger = getLogger(__name__)
basicConfig(level=DEBUG)


class Function(ABC):
    @abstractmethod
    def f(self, x: np.ndarray) -> np.ndarray:
        pass


def g(t: float) -> float:
    return float(f(int(t)))


if __name__ == "__main__":
    a: int = 1
    b: float = g(a)
    print(__name__, __package__)
