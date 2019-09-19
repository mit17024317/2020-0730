#!/usr/bin/env python3
import numpy as np
from ego import EGO

from model import FuzzyCM
from model import GroupingModel

if __name__ == "__main__":
    print("-- optimize start --")

    # test function
    def f(x: float):
        sum = np.sum(x)
        return np.sin(np.sqrt(sum)*10.0)

    # print("--- GroupingModel optimize ---")
    # ego = EGO(f, 2, GroupingModel)
    # ego.optimize(30)
    # print("min:", np.array(ego.min).T)
    # print("RMSE:", np.array(ego.RMSE).T)
    # print("--- finish ---")

    print("--- FuzzyCM optimize ---")
    ego = EGO(f, 1, FuzzyCM)
    ego.optimize(30)
    print("min:", np.array(ego.min).T)
    print("RMSE:", np.array(ego.RMSE).T)
    print("--- finish ---")

