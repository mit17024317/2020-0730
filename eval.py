#!/usr/bin/env python3
"""
Evalation method
"""

import sys
from model import FuzzyCM
from model import GPR
from pyDOE import lhs
import matplotlib.pyplot as plt
import numpy as np
import random


def RMSE(dim, func, model, size=10000):
    """
    normal RMSE

    Parameters
    ----------
    dim : int
        dimension of problem
    func : function: array:double -> double
        True Function
    model : ModelInterface
        func's model
    size : int
        point of rmse size

    Returns
    -------
    rmse : double
        rmse value of model
    """
    if dim > RMSE.max:
        print("!! eval.py RMSE error !!")
        print("update RMSE.max greater than ", dim)
        sys.exit()
    if RMSE.dataset[dim] == []:
        RMSE.dataset[dim] = \
            np.array([[random.random() for k in range(dim)]
                      for i in range(size)])

    sum = 0.0
    for data in RMSE.dataset[dim]:
        sum += (func(data)-model.getPredict(data)[0])**2
    rmse = np.sqrt(sum/size)

    return rmse


def RMSE_G(dim, func, model, size=10000, size_T=500):
    """
    near good point RMSE

    Parameters
    ----------
    dim : int
        dimension of problem
    func : function: array:double -> double
        True Function
    model : ModelInterface
        func's model
    size : int
        point of rmse size
    size_T : int
        point of rmse size near good point

    Returns
    -------
    rmse : double
        rmse value of model
    """
    if dim > RMSE.max:
        print("!! eval.py RMSE error !!")
        print("update RMSE.max greater than ", dim)
        sys.exit()
    if len(RMSE.dataset[dim]) > 0:
        RMSE.dataset[dim] = \
            np.array([[random.random() for k in range(dim)]
                      for i in range(size)])

    sum = 0.0
    lst = []
    for data in RMSE.dataset[dim]:
        lst.append([func(data), model.getPredict(data)[0]])
    lst = sorted(lst)
    for l in lst[:size_T]:
        sum += (l[0]-l[1])**2
    rmse = np.sqrt(sum/size_T)

    return rmse


def RMSE_P(dim, func, model, newIndiv, size=10000, size_T=500):
    """
    near new individual RMSE

    Parameters
    ----------
    dim : int
        dimension of problem
    func : function: array:double -> double
        True Function
    model : ModelInterface
        func's model
    newIndiv : array:double
        new individual
    size : int
        point of rmse size
    size_T : int
        point of rmse size near new individual

    Returns
    -------
    rmse : double
        rmse value of model
    """
    # set dataset 
    if dim > RMSE.max:
        print("!! eval.py RMSE error !!")
        print("update RMSE.max greater than ", dim)
        sys.exit()
    if len(RMSE.dataset[dim]) > 0:
        RMSE.dataset[dim] = \
            np.array([[random.random() for k in range(dim)]
                      for i in range(size)])

    sum = 0.0
    lst = []
    for data in RMSE.dataset[dim]:
        norm = np.linalg.norm(data-newIndiv)
        lst.append([norm, func(data), model.getPredict(data)[0]])
    lst = sorted(lst)
    for l in lst[:size_T]:
        sum += (l[1]-l[2])**2
    rmse = np.sqrt(sum/size_T)

    return rmse


RMSE.max = 101
RMSE.dataset = [[] for i in range(RMSE.max+1)]


if __name__ == "__main__":
    # debug parameter
    SIZE = 50

    # test function
    def f(x: float):
        x = (x*1000.0)-500.0
        v = [t*np.sin(np.sqrt(abs(t))) for t in x]
        return sum(v)

    sampleX = [i for i in range(10, 20)]
    sampleY = []
    for DIM in sampleX:
        print("dimension", DIM, sep=": ")

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
