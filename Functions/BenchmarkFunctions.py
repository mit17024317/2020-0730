#!/usr/bin/env python3
"""Benchmark Function Interface."""

__author__ = "R.Nakata"
__date__ = "2020/02/04"


import numpy as np


class Rosenbrock:
    def f(self, x: np.ndarray, obj: int = 1) -> np.ndarray:
        sum = 0
        for i in range(len(x) - 1):
            sum += (
                100 * (10 * x[i + 1] - 5 - (10 * x[i] - 5) ** 2) ** 2
                + (1 - 10 * x[i] - 5) ** 2
            )
        return np.array([sum])


class Rastrigin:
    def f(self, x: np.ndarray, obj: int = 1) -> np.ndarray:
        n = len(x)
        sum = 10 * n
        for t in x:
            t = 5.12 * 2 * t - 5.12
            sum += t ** 2 - 10 * np.cos(2 * np.pi * t)
        return np.array([sum])


class Schwefel:
    def f(self, x: np.ndarray, obj: int = 1) -> np.ndarray:
        sum = 0
        for t in x:
            t = 1000 * t - 500
            sum -= t * np.sin(np.sqrt(np.abs(t)))
        return np.array([sum])
