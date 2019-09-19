#!/usr/bin/env python3
import GPy
import numpy as np
import matplotlib.pyplot as plt
from pyDOE import lhs


def f(x):
    return np.sum(x**2)/len(x)


def gpr(dim):
    kernel = GPy.kern.RBF(dim)+GPy.kern.Matern32(dim)

    x = np.array([[s[i] for i in range(dim)] for s in lhs(dim, 50, "c")])
    y = np.array([f(t) for t in x])

    model = GPy.models.GPRegression(x, y[:, None], kernel=kernel)
    model.optimize()

    return model


if __name__ == "__main__":

    NUM = 30

    for dim in range(1,50):
        print("-- {} --".format(dim))
        for _ in range(NUM):
            model = gpr(dim)
            print("|")
        print()
