#!/usr/bin/env python3

import sys
from model import FuzzyCM
from model import GPR
from pyDOE import lhs
import matplotlib.pyplot as plt
import numpy as np
import random


def RMSE(dim, func, model):
    size = 10000
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


RMSE.max = 101
RMSE.dataset = [[] for i in range(RMSE.max+1)]


if __name__ == "__main__":
    # debug parameter
    SIZE = 50

    # test function
    def f(x: float):
        sum = np.sum(x)
        sum = np.sin(np.sqrt(sum)*10.0)
        return sum

    sampleX = [i for i in range(1, 50)]
    sampleY = []
    for DIM in sampleX:

        # create sample point
        X = np.array([[s[i] for i in range(DIM)] for s in lhs(DIM, SIZE)])
        Y = np.array([f(i) for i in X]) 
        model = FuzzyCM(X, Y)
        
        # calc RMSE
        val = RMSE(DIM, f, model)
        sampleY.append(val)
        print("dim= ", DIM, ": ", val)
    
    plt.plot(sampleX, sampleY, marker=".", markersize=10, c="black")
    plt.legend()

    plt.xlabel("dimension")
    plt.ylabel("RMSE")

    plt.savefig("./fig.png")
