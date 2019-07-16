#!/usr/bin/env python3
import os
import numpy as np
from ego import EGO

from model import FuzzyCM
from model import GroupingModel

from function import Schwefel


def out(ego, txt):
    with open("ex/min/{}.txt".format(txt), "a") as f:
        for x in ego.min:
            f.write(str(x)+", ")
        f.write("\n")
    with open("ex/rmse/{}.txt".format(txt), "a") as f:
        for x in ego.RMSE:
            f.write(str(x)+", ")
        f.write("\n")


if __name__ == "__main__":
    print("-- optimize start --")
    END = 100
    os.remove("./ex/min/mix.txt")
    os.remove("./ex/rmse/mix.txt")


    for i in range(10):
        print("--- new EGO optimize ---")
        ego = EGO(Schwefel, 20, [FuzzyCM, GroupingModel])
        ego.optimize(END)
        out(ego, "mix")
        print("--- finish ---")

        print("--- GroupingModel optimize ---")
        ego = EGO(Schwefel, 20, [GroupingModel])
        ego.optimize(END)
        out(ego, "Group")
        print("--- finish ---")

        print("--- FuzzyCM optimize ---")
        ego = EGO(Schwefel, 20, [FuzzyCM])
        ego.optimize(END)
        out(ego, "Norm")
        print("--- finish ---")

