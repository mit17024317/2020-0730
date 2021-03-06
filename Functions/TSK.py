#!/usr/bin/env python3
"""TSK Problem."""

__author__ = "R.Nakata"
__date__ = "2020/04/10"


import csv
import os
import subprocess
import sys
from logging import DEBUG, basicConfig, getLogger
from typing import List

import numpy as np
from mypythontools.Design import Singleton

from .FunctionInterface import FunctionInterface

logger = getLogger()


class TSK:
    # NOTE 圧力最悪値を大きめに取っているつもりだが，これ以上の値も出得る
    output_low_upper = [[0, 200], [50, 100000]]
    simulatorDir = "/home/kaiseki/work/"

    def __init__(
        self, probDir: str, input_low_upper: List[List[float]], units: List[str]
    ) -> None:
        self.probDir: str = probDir
        self.input_low_upper: List[List[float]] = input_low_upper
        self.units: List[str] = units

    def __writeDesign(self, x: np.ndarray):
        # [0:1] to [l:u]
        x = np.array(
            [t * (lu[1] - lu[0]) + lu[0] for t, lu in zip(x, self.input_low_upper)]
        )
        writeFile = self.simulatorDir + self.probDir + "input_2019R3.txt"
        with open(writeFile, "w") as f:
            for t, u in zip(x, self.units):
                f.write(str(t))
                f.write(f" [{u}]\n")

    def __readObj(self) -> np.ndarray:
        #  [l:u] to [0:1]
        y = []
        readFile = self.simulatorDir + self.probDir + "output_2019R3.txt"
        with open(readFile, "r") as f:
            reader = csv.reader(f)
            for lineV in reader:
                line = lineV[0]
                if "[C]" in line or "[K]" in line:
                    val = float(line.split(" [")[0])
                    lu = self.output_low_upper[0]
                    y.append((val - lu[0]) / (lu[1] - lu[0]))
                if "[Pa]" in line:
                    val = float(line.split(" [")[0])
                    lu = self.output_low_upper[1]
                    y.append((val - lu[0]) / (lu[1] - lu[0]))
            return np.array(y)

    def __exe(self) -> None:
        os.chdir(self.simulatorDir + self.probDir)
        sh: str = self.simulatorDir + self.probDir + "wb2019R3_Nakata.sh"
        subprocess.run(sh)
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

    def f(self, x: np.ndarray, obj) -> np.ndarray:
        # input
        self.__writeDesign(x)
        # run
        self.__exe()
        # output
        val: np.ndarray = self.__readObj()
        return val


class TSK1(Singleton):

    input_low_upper: List[List[float]] = [
        [0.02, 0.133],
        [0.02, 0.133],
        [0, 0.5],
        [-0.0665, 0.0665],
        [-0.0665, 0.0665],
        [-90, 90],
    ]
    units: List[str] = ["m" for _ in range(5)] + ["degree"]
    probDir: str = "orifice1_200515/"

    def f(self, x: np.ndarray, obj) -> np.ndarray:
        if not obj == 2 or not len(x) == 6:
            logger.critical("#obj must be 2 on TSK1 problems")
            logger.critical("#dim must be 6 on TSK1 problems")
            logger.critical("--- forced termination ---")
            sys.exit()
        tsk: FunctionInterface = TSK(self.probDir, self.input_low_upper, self.units)
        val: np.ndarray = tsk.f(x, obj)
        return val


class TSK2(Singleton):

    input_low_upper: List[List[float]] = [
        [0, 0.5],
        [0.001, 0.3],
        [0.001, 0.3],
        [0.001, 0.3],
        [0.001, 0.3],
        [0.001, 0.3],
        [0.001, 0.3],
    ]
    units: List[str] = ["m" for _ in range(7)]
    probDir: str = "orifice2_200601/"

    def f(self, x: np.ndarray, obj) -> np.ndarray:
        if not obj == 2 or not len(x) == 7:
            logger.critical("#obj must be 2 on TSK2 problems")
            logger.critical("#dim must be 7 on TSK2 problems")
            logger.critical("--- forced termination ---")
            sys.exit()
        tsk: FunctionInterface = TSK(self.probDir, self.input_low_upper, self.units)
        val: np.ndarray = tsk.f(x, obj)
        return val


if __name__ == "__main__":
    basicConfig(level=DEBUG)

    x = np.array([0.3 for _ in range(6)])

    t = TSK1()
    val = t.f(x, 2)
    logger.debug(val)
