#!/usr/bin/env python3
"""TSK Problem."""

__author__ = "R.Nakata"
__date__ = "2020/04/10"


import numpy as np
from mypythontools.Design import Singleton


class TSK03(Singleton):
    def __writeDesign(self, x: np.ndarray, name="~/work/opt/pipe03/input_2019R3.txt"):
        with open(name, "w") as f:
            for t in x[:-1]:
                f.write(t)
                f.write(" [m]\n")
            f.write(t[-1])
            f.write(" [degree]\n")

    def __readObj(self):
        ...

    def f(self, x: np.ndarray, obj: int = 2) -> np.ndarray:
        ...
