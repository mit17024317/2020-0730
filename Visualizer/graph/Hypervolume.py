#!/usr/bin/env python3
"""Hypervolume visualizer."""

__author__ = "R.Nakata"
__date__ = "2020/02/17"

from typing import List

import matplotlib.pyplot as plt
import numpy as np


class HypervolumeVisualizer:
    def __init__(self, frm: int):
        self.frm: int = frm
        self.__setting()

    def __setting(self) -> None:
        plt.legend()
        plt.xlabel("Number of evaluations")
        plt.ylabel("Hypervolume")

    def addToPlt(self, data: np.ndarray, name: str) -> None:
        x: List[int] = [x + self.frm for x in range(len(data))]
        plt.plot(x, data, label=name)

    def saveAndShow(self, filename):
        plt.savefig(f"Visualizer/out/{filename}")
        self.show()

    def show(self):
        plt.show()
