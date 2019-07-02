#!/usr/bin/env python3
import numpy as np
from ego import EGO

from model import FuzzyCM
from model import GroupingModel

from function import Schwefel

if __name__ == "__main__":
    print("-- optimize start --")
    END = 100


    print("--- GroupingModel optimize ---")
    ego = EGO(Schwefel, 20, [GroupingModel])
    ego.optimize(END)
    with open("ex/1.txt", "w") as f:
        for x in ego.min:
            f.write(str(x)+", ")
        f.write("\n")
        for x in ego.RMSE:
            f.write(str(x)+", ")
    print("--- finish ---")

    print("--- FuzzyCM optimize ---")
    ego = EGO(Schwefel, 20, [FuzzyCM, GroupingModel])
    ego.optimize(END)
    with open("ex/2.txt", "w") as f:
        for x in ego.min:
            f.write(str(x)+", ")
        f.write("\n")
        for x in ego.RMSE:
            f.write(str(x)+", ")
    print("--- finish ---")

    print("--- new EGO optimize ---")
    ego = EGO(Schwefel, 20, [FuzzyCM, GroupingModel])
    ego.optimize(END)
    with open("ex/3.txt", "w") as f:
        for x in ego.min:
            f.write(str(x)+", ")
        f.write("\n")
        for x in ego.RMSE:
            f.write(str(x)+", ")
    print("--- finish ---")

