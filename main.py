#!/usr/bin/env python3
import os
import numpy as np
from ego import EGO

from model import FuzzyCM
from model import GroupingModel

from function import Schwefel
from function import Rosenbrock
from function import Rastrigin


def out(ego, txt):
    with open("ex/min/{}.txt".format(txt), "a") as f:
        for x in ego.min:
            f.write(str(x)+", ")
        f.write("\n")
    with open("ex/rmse/{}.txt".format(txt), "a") as f:
        for x in ego.RMSE:
            f.write(str(x)+", ")
        f.write("\n")
    with open("ex/models/{}.txt".format(txt), "a") as f:
        for x in ego.useModels:
            f.write(str(x)+", ")
        f.write("\n")


if __name__ == "__main__":
    print("-- optimize start --")
    END = 150

    func = Schwefel

    for i in range(30):
        print("--- new EGO optimize ---")
        ego = EGO(func, 50, [FuzzyCM, GroupingModel])
        ego.optimize(END)
        out(ego, "mix")
        print("--- finish ---")

        print("--- GroupingModel optimize ---")
        ego = EGO(func, 50, [GroupingModel])
        ego.optimize(END)
        out(ego, "Group")
        print("--- finish ---")

        print("--- FuzzyCM optimize ---")
        ego = EGO(func, 50, [FuzzyCM])
        ego.optimize(END)
        out(ego, "Norm")
        print("--- finish ---")
