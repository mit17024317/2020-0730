#!/usr/bin/env python3
"""Linear Basis Function Model."""

__author__ = "R.Nakata"
__date__ = "2019/11/01"

from abc import ABC, abstractmethod
from logging import DEBUG, basicConfig, getLogger

import numpy as np

logger = getLogger(__name__)
basicConfig(level=DEBUG)


class Function(ABC):
    @abstractmethod
    def f(self, x: np.ndarray) -> np.ndarray:
        pass


def test(t: int) -> int:
    return 1


if __name__ == "__main__":
    a: int = 1
    test(a)
