#!/usr/bin/env python3
"""Linear Basis Function Model."""

__author__ = "R.Nakata"
__date__ = "2019/11/01"

from abc import ABC, abstractmethod
from logging import DEBUG, basicConfig, getLogger

import numpy as np

logger = getLogger(__name__)
basicConfig(level=DEBUG)


def Rosenbrock(x):
    sum = 0
    for i in range(len(x) - 1):
        sum += (
            100 * (10 * x[i + 1] - 5 - (10 * x[i] - 5) ** 2) ** 2
            + (1 - 10 * x[i] - 5) ** 2
        )
    return sum / 5000


def Rastrigin(x):
    n = len(x)
    sum = 10 * n
    for t in x:
        t = 5.12 * 2 * t - 5.12
        sum += t ** 2 - 10 * np.cos(2 * np.pi * t)
    return sum / 1000


def Schwefel(x):
    sum = 0
    for t in x:
        t = 1000 * t - 500
        sum -= t * np.sin(np.sqrt(np.abs(t)))
    return sum / 3000


def original1(x):
    sum = np.sum(x)
    return np.sin(np.sqrt(sum) * 10.0)


def original2(x):
    p = int(len(x) / 2)
    a = 1
    b = 1
    for i in range(p):
        a *= x[i]
    for i in range(p, len(x)):
        b *= x[i]
    return a + b


def easyFunc(x):
    val = 0.0
    for t in x:
        val += t ** 2
    return val
