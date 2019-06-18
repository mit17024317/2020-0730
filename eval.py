#!/usr/bin/env python3

import sys
from model import FuzzyCM
from model import GPR
from pyDOE import lhs
import matplotlib.pyplot as plt
import numpy as np
import random


def RMSE(dim, func, model):
    size = 1000
    if dim > RMSE.max:
        print("!! eval.py RMSE error !!")
        print("update RMSE.max greater than ", dim)
        sys.exit()
    if RMSE.dataset[DIM] == []:
        RMSE.dataset[DIM] = \
            np.array([[random.random() for k in range(DIM)]
                      for i in range(size)])

    v = np.array([f(i) for i in RMSE.dataset[DIM]]) - \
        model.getPredictValue(RMSE.dataset[DIM])
    v = pow(v, 2)
    return np.sqrt(np.sum(v)/size)

RMSE.max = 50
RMSE.dataset = [[] for i in range(RMSE.max+1)]


if __name__ == "__main__":
    # debug parameter
    DIM = 1 
    SIZE = 300

    # test function
    def f(x: float):
        sum = np.sum(x)
        return np.sin(np.sqrt(sum)*10.0)

    print("-- create model-- ")
    # create sample point
    X = np.array([[s[i] for i in range(DIM)] for s in lhs(DIM, SIZE)])
    Y = np.array([f(i) for i in X]) 
    model1 = FuzzyCM(X, Y)
    # model2 = GPR(X, Y)
    
    val = RMSE(DIM, f, model1)
    print(val)
    # val = RMSE(DIM, f, model2)
    print(val)

    if DIM == 1:
        # create sample point for debug
        ALL_X = np.linspace(0.0, 1.0, 500)[:, None]
        ALL_Y_TRUE = [f(x) for x in ALL_X]
        ALL_Y_FUZZY = model1.getPredictValue(ALL_X)

        print("-- create figure-- ")
        # create model figure
        plt.plot(ALL_X, ALL_Y_TRUE, c="r", label='function')
        # plt.plot(ALL_X, ALL_Y_GPR, c="b", label='GPR')
        plt.plot(ALL_X, ALL_Y_FUZZY, c="y", label='Fuzzy CM')
        plt.plot(X, Y, 'o', marker=".", markersize=10, c="black", label="sample point")
        plt.legend()

        plt.xlabel("X")
        plt.ylabel("Y")

        plt.savefig("./fig.png")
    print("--- finish ---")
