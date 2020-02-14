#!/usr/bin/env python3
"""ZDT Test Problem."""

__author__ = "R.Nakata"
__date__ = "2020/02/12"


import numpy as np


class ZDT4:
    def f(self, x: np.ndarray) -> np.ndarray:
        N: int = len(x)
        f1: float = x[0]
        g: float = 1 + 10 * (N - 1) + np.sum(
            [t / 5 * t / 5 - 10 * np.cos(4 * np.pi * t / 5) for t in x[1:]]
        )
        h: float = 1 - np.sqrt(f1 / g)
        f2: float = g * h / (20 * (N - 1))
        return np.array([f1, f2])


class ZDT6:
    def f(self, x: np.ndarray) -> np.ndarray:
        N: int = len(x)
        f1: float = 1 - np.exp(-4 * x[0]) * np.power(np.sin(6 * np.pi * x[0]), 6)
        g: float = 1 + 9 * np.power(np.sum(x[1:]) / (N - 1), 1 / 4)
        f2: float = g * (1 - np.power(f1 / g, 2)) / 10
        return np.array([f1, f2])
