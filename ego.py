#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import random
from pyDOE import lhs
from model import FuzzyCM
from scipy import integrate
from scipy.stats import norm


class EGO:
    def __print(self):
        if len(self.X[0]) == 1:
            # create sample point for debug
            ALL_X = np.linspace(0.0, 1.0, 500)[:, None]
            ALL_Y_TRUE = [self.f(x) for x in ALL_X]
            ALL_Y = self.model.getPredictValue(ALL_X)

            print("-- create figure-- ")
            # create model figure
            plt.figure()
            plt.plot(ALL_X, ALL_Y_TRUE, c="r", label='function')
            plt.plot(ALL_X, ALL_Y, c="y", label='Fuzzy CM')
            plt.plot(self.X, self.Y, 'o', marker=".", markersize=10, c="black", label="sample point")
            plt.legend()

            plt.xlabel("X")
            plt.ylabel("Y")
            plt.savefig("./ego/fig{0}.png".format(self.eval))

    def __sampling(self):
        self.SIZE = 10
        # create sample point
        self.X = np.array([[s[i] for i in range(self.dim)] for s in lhs(self.dim, self.SIZE)])
        self.Y = np.array([self.f(i) for i in self.X])

    def __EI(self, x):

        m, v = self.model.getPredict(x)
        m = m[0]
        s = np.sqrt(v[0])

        return norm.cdf(self.min, m, s)[0]


    def optimize(self, evalationNum):
        for _ in range(evalationNum - self.SIZE):
            print("{0}th eval".format(self.eval))

            max = -1.0
            newInd = []
            self.eval += 1
            for _ in range(100):
                x = [random.random() for _ in range(self.dim)]
                val = self.__EI(x)
                if val > max:
                    newInd = x
                    max = val
            self.X = np.array(np.append(self.X, [newInd], axis=0))
            self.Y = np.append(self.Y, self.f(newInd))
            self.model = FuzzyCM(self.X, self.Y)
            self.__print()


    def __init__(self, f, dim, model=FuzzyCM):
        self.eval = 0
        self.f = f
        self.dim = dim
        self.__sampling()
        self.model = model(self.X, self.Y)
        self.min = np.amin(self.Y)
        self.__print()


if __name__ == "__main__":

    # test function
    def f(x: float):
        sum = np.sum(x)
        return np.sin(np.sqrt(sum)*10.0)

    print("--- start ---")
    # ego = EGO(f, 1, FuzzyCM)
    ego = EGO(f, 2)
    print("-- optimize --")
    ego.optimize(15)
    print("--- finish ---")
