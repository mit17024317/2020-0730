#!/usr/bin/env python3
from abc import ABC, abstractmethod
import GPy
import numpy as np
from skfuzzy.cluster import cmeans
import matplotlib.pyplot as plt
from pyDOE import lhs


class modelInterface(ABC):
    @abstractmethod
    def getPredictValue(self, x: float):
        pass

class GPR(modelInterface):

    def __init__(self, sampleX: list, sampleY: list):
        DIM = sampleX[0].size
        kernel = GPy.kern.RBF(DIM)+GPy.kern.Matern32(DIM)
        self.model = GPy.models.GPRegression(sampleX, sampleY[:, None], kernel=kernel)
        self.model.optimize()

    def getPredictValue(self, x: list):
        return [val[0] for val in
                self.model.predict_quantiles(
                    x,
                    quantiles=(2.5, 50, 97.5)
                )[1]]


class FuzzyCM(modelInterface):

    def __init__(self, sampleX: list, sampleY: list):
        DIM = sampleX[0].size

        # data, m, c, error, maxIter, init, seed
        # center, result, firstResult, distance?, ?, loopNum, ?
        self.models = []
        cntr, u, u0, d, jm, p, fpc = cmeans(sampleX.T, 3, 3.0,  0.01, 1000)
        for c, x in zip(cntr, u):
            kernel = GPy.kern.RBF(DIM)+GPy.kern.Matern32(DIM)
            arg = np.argsort(x)[::-1]
            X = np.array([sampleX[t] for t in arg[:10]])
            Y = np.array([sampleY[t] for t in arg[:10]])
            mdl = GPy.models.GPRegression(X, Y[:, None], kernel=kernel)
            mdl.optimize()
            self.models.append({"m": mdl, "c": c})

    def getPredictValue(self, x: list):
        return [val[0] for val in
                self.models[0]["m"].predict_quantiles(
                    x,
                    quantiles=(2.5, 50, 97.5)
                )[1]]


if __name__ == "__main__":
    # debug parameter
    DIM = 1
    SIZE = 30 

    # test function
    def f(x: float):
        sum = np.sum(x)
        return np.sin(np.sqrt(sum)*10.0)

    print("-- create model-- ")
    # create sample point
    X = np.array([[s[i] for i in range(DIM)] for s in lhs(DIM, SIZE)])
    Y = np.array([f(i) for i in X])
    # rint(X)

    # create model
    MODEL = GPR(X, Y)
    MODEL_FUZZY = FuzzyCM(X, Y)

    if DIM == 1:
        # create sample point for debug
        ALL_X = np.linspace(0.0, 1.0, 500)[:, None]
        ALL_Y_TRUE = [f(x) for x in ALL_X]
        ALL_Y_GPR = MODEL.getPredictValue(ALL_X)
        ALL_Y_FUZZY = MODEL_FUZZY.getPredictValue(ALL_X)

        print("-- create figure-- ")
        # create model figure
        plt.plot(ALL_X, ALL_Y_TRUE, c="r", label='function')
        plt.plot(ALL_X, ALL_Y_GPR, c="b", label='GPR')
        plt.plot(ALL_X, ALL_Y_FUZZY, c="y", label='Fuzzy CM')
        plt.plot(X, Y, 'o', marker=".", markersize=10, c="black", label="sample point")
        plt.legend()

        plt.xlabel("X")
        plt.ylabel("Y")

        plt.savefig("./fig.png")
    print("--- finish ---")
