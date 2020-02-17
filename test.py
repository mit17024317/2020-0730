#!/usr/bin/env python3
"""Hypervolume visualizer."""

__author__ = "R.Nakata"
__date__ = "2020/02/17"

from typing import List

import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    x = [i for i in range(100)]
    y = [i * i for i in range(100)]
    y2 = [100 * i for i in range(100)]

    plt.plot(x, y, label="ok")
    plt.plot(x, y2, label="ng")

    plt.legend()
    plt.xlabel("Number of evaluations")
    plt.ylabel("Hypervolume")

    plt.show()
    plt.savefig("Visualizer/out/sample.png")
