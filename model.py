#!/usr/bin/env python3
from abc import ABC, abstractmethod
import GPy
import numpy as np
import matplotlib.pyplot as plt
from pyDOE import lhs


class modelInterface(ABC):
    @abstractmethod
    def getPredictValue(self, x: float):
        pass

class GPR(modelInterface):

    def __init__(self, sampleX: list, sampleY: list):
        kernel = GPy.kern.RBF(1)+GPy.kern.Matern32(1)
        self.model = GPy.models.GPRegression(sampleX[:, None], sampleY[:, None], kernel=kernel)
        self.model.optimize()

    def getPredictValue(self, x: list):
        return [val[0] for val in
                self.model.predict_quantiles(
                    x[:, None],
                    quantiles=(2.5, 50, 97.5)
                )[1]]


class FuzzyCM(modelInterface):

    def __init__(self, sampleX: list, sampleY: list):
        kernel = GPy.kern.RBF(1)+GPy.kern.Matern32(1)
        self.model = GPy.models.GPRegression(sampleX[:, None], sampleY[:, None], kernel=kernel)
        self.model.optimize()

    def getPredictValue(self, x: list):
        return [val[0] for val in
                self.model.predict_quantiles(
                    x[:, None],
                    quantiles=(2.5, 50, 97.5)
                )[1]]


if __name__ == "__main__":
    # test function
    def f(x: float):
        return np.sin(np.sqrt(x)*10.0)

    print("-- create model-- ")
    # create sample point
    SIZE = 10
    X = np.array([s[0] for s in lhs(1, SIZE)])
    Y = np.array([f(i) for i in X])
    print(X)

    # create model
    MODEL = GPR(X, Y)
    MODEL_FUZZY = FuzzyCM(X, Y)

    # create sample point for debug
    ALL_X = np.linspace(0.0, 1.0, 500)
    ALL_Y_TRUE = f(ALL_X)
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
