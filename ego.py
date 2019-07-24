#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import random
from pyDOE import lhs
from model import FuzzyCM
from model import GroupingModel
from modelSelect import SelectModel
from scipy import integrate
from scipy.stats import norm
from eval import RMSE


class EGO:
    def __print(self):
        if len(self.X[0]) == 1:
            # create sample point for debug
            ALL_X = np.linspace(0.0, 1.0, 500)[:, None]
            ALL_Y_TRUE = [self.f(x) for x in ALL_X]
            ALL_Y = self.modelSelecter.getModel().getPredictValue(ALL_X)

            print("-- create figure-- ")
            # create model figure
            plt.figure()
            plt.plot(ALL_X, ALL_Y_TRUE, c="r", label='function')
            plt.plot(ALL_X, ALL_Y, c="y", label='Fuzzy CM')
            plt.plot(self.X, self.Y, 'o', marker=".",
                     markersize=10, c="black", label="sample point")
            plt.legend()

            plt.xlabel("X")
            plt.ylabel("Y")
            plt.savefig("./ego/fig{0}.png".format(self.eval))

    def __sampling(self):
        self.SIZE = 50
        # create sample point
        self.X = np.array([[s[i] for i in range(self.dim)]
                           for s in lhs(self.dim, self.SIZE)])
        self.Y = np.array([self.f(i) for i in self.X])

    def __EI(self, x):

        m, v = self.modelSelecter.getModel().getPredict(x)
        m = m[0]
        s = np.sqrt(v[0])
        nm = (self.min[-1] - m) / s
        return nm * s * norm.cdf(nm, 0, 1)[0] + s * norm.pdf(nm, 0, 1)[0]

    def optimize(self, evalationNum):
        for _ in range(evalationNum - self.SIZE):
            print("{0}th eval".format(self.eval))

            max = -1.0
            newInd = []
            self.eval += 1
            for _ in range(1000):
                x = [random.random() for _ in range(self.dim)]
                val = self.__EI(x)
                if val > max:
                    newInd = x
                    max = val
            y = self.f(newInd)
            self.X = np.array(np.append(self.X, [newInd], axis=0))
            self.Y = np.append(self.Y, self.f(newInd))
            self.modelSelecter.update(newInd, y, self.X, self.Y)
            self.useModels.append(
                self.modelSelecter.getModel().__class__.__name__)
            self.min.append(np.amin(self.Y))
            self.RMSE.append(
                RMSE(self.dim, self.f, self.modelSelecter.getModel()))
            self.__print()

    def __init__(self, f, dim, models=[FuzzyCM]):
        self.eval = 0
        self.f = f
        self.dim = dim
        self.__sampling()
        self.modelSelecter = SelectModel(models, self.X, self.Y)
        self.min = [np.amin(self.Y)]
        self.RMSE = [RMSE(dim, f, self.modelSelecter.getModel())]
        self.useModels = [self.modelSelecter.getModel().__class__.__name__]
        self.__print()


if __name__ == "__main__":

    # test function
    def f(x: float):
        return np.sin(x[0]*100)

    print("--- start ---")
    ego = EGO(f, 1, [FuzzyCM, GroupingModel])
    print("-- optimize --")
    ego.optimize(60)
    print("--- finish ---")
