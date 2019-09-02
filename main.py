#!/usr/bin/env python3
import os
import numpy as np
from ego import EGO

from model import FuzzyCM
from model import GroupingModel

from function import Schwefel
from function import Rosenbrock
from function import Rastrigin
import function


def createDir(func, dim):
    dir = "./result/"
    if not os.path.exists(dir):
        os.mkdir(dir)

    dir += "{}_{}/".format(func, dim)
    if not os.path.exists(dir):
        os.mkdir(dir)

    return dir


def out(ego, func, dim, txt):
    dir = createDir(func, dim)

    with open(dir+"min_{}.csv".format(txt), "a") as f:
        for x in ego.min:
            f.write(str(x)+", ")
        f.write("\n")
    with open(dir+"rmse_{}.csv".format(txt), "a") as f:
        for x in ego.RMSE:
            f.write(str(x)+", ")
        f.write("\n")
    with open(dir+"rmseg_{}.csv".format(txt), "a") as f:
        for x in ego.RMSE_G:
            f.write(str(x)+", ")
        f.write("\n")
    with open(dir+"rmsep_{}.csv".format(txt), "a") as f:
        for x in ego.RMSE_P:
            f.write(str(x)+", ")
        f.write("\n")
    with open(dir+"distance_{}.csv".format(txt), "a") as f:
        for a, m in ego.distance:
            f.write(str(a)+", "+str(m)+"\n")
    with open(dir+"models_{}.csv".format(txt), "a") as f:
        for x in ego.useModels:
            f.write(str(x)+", ")
        f.write("\n")


if __name__ == "__main__":
    print("-- optimize start --")
    END = 100
    DIM = 50

    func = function.Rastrigin
    func_name = "Rastrigin"

    for i in range(10):
        print("--- FuzzyCM optimize ---")
        ego = EGO(func, DIM, [FuzzyCM])
        ego.optimize(END)
        out(ego, func_name, DIM, "norm")
        print("--- finish ---")

        print("--- GroupingModel optimize ---")
        ego = EGO(func, DIM, [GroupingModel])
        ego.optimize(END)
        out(ego, func_name, DIM, "group")
        print("--- finish ---")

        print("--- new EGO optimize ---")
        ego = EGO(func, DIM, [FuzzyCM, GroupingModel])
        ego.optimize(END)
        out(ego, func_name, DIM, "mix")
        print("--- finish ---")

