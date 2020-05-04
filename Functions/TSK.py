#!/usr/bin/env python3
"""TSK Problem."""

__author__ = "R.Nakata"
__date__ = "2020/04/10"


import subprocess
from logging import getLogger

import numpy as np
from mypythontools.Design import Singleton

logger = getLogger()

input_low_upper = [
    [0, 0.5],
    [0.02, 0.133],
    [0.02, 0.133],
    [-0.655, 0.655],
    [-0.655, 0.655],
    [-90, 90],
]
# NOTE 圧力最悪値を1000から3000に更新している
output_low_upper = [[0, 200], [50, 3000]]


class TSK03(Singleton):
    def __writeDesign(
        self, x: np.ndarray, name="/home/kaiseki/work/opt/pipe03/input_2019R3.txt"
    ):
        # [0:1] to [l:u]
        x = np.array([t * (lu[1] - lu[0]) + lu[0] for t, lu in zip(x, input_low_upper)])
        with open(name, "w") as f:
            for t in x[:-1]:
                f.write(str(t))
                f.write(" [m]\n")
            f.write(str(x[-1]))
            f.write(" [degree]\n")

    def __readObj(
        self, name="/home/kaiseki/work/opt/pipe03/output_2019R3.txt"
    ) -> np.ndarray:
        #  [l:u] to [0:1]
        with open(name, "r") as f:
            line = f.read()
            out = line.split("[degree]?n")[1].split(" [C]?n")
            a = float(out[0])
            b = float(out[1].split(" [Pa]")[0])
            y = [
                (t - lu[0]) / (lu[1] - lu[0]) for t, lu in zip([a, b], output_low_upper)
            ]
            return np.array(y)

    def __exe(
        self, name="/home/kaiseki/work/opt/pipe03/wb2019R3CentOS_Nakata.sh"
    ) -> None:
        subprocess.run(name)

    def f(self, x: np.ndarray, obj: int = 2) -> np.ndarray:
        # input
        self.__writeDesign(x)
        # run
        self.__exe()
        # output
        val: np.ndarray = self.__readObj()
        return val


if __name__ == "__main__":
    x = np.array([0.3 for _ in range(6)])
    p = TSK03()
    val = p.f(x)
    logger.info(val)
