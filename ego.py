#!/usr/bin/env python3
from pyDOE import lhs
import numpy as np
from model import FuzzyCM
import matplotlib.pyplot as plt
from scipy import integrate


class EGO:
    def __print(self):
        if len(self.X[0]) == 1:
            # create sample point for debug
            ALL_X = np.linspace(0.0, 1.0, 500)[:, None]
            ALL_Y_TRUE = [f(x) for x in ALL_X]
            # ALL_Y_GPR = MODEL.getPredictValue(ALL_X)
            ALL_Y = self.model.getPredictValue(ALL_X)

            print("-- create figure-- ")
            # create model figure
            plt.figure()
            plt.plot(ALL_X, ALL_Y_TRUE, c="r", label='function')
            # plt.plot(ALL_X, ALL_Y_GPR, c="b", label='GPR')
            plt.plot(ALL_X, ALL_Y, c="y", label='Fuzzy CM')
            plt.plot(self.X, self.Y, 'o', marker=".", markersize=10, c="black", label="sample point")
            plt.legend()

            plt.xlabel("X")
            plt.ylabel("Y")
            self.eval += 1
            plt.savefig("./ego/fig{0}.png".format(self.eval))

    def __sampling(self, dim):
        SIZE = 20
        # create sample point
        self.X = np.array([[s[i] for i in range(dim)] for s in lhs(dim, SIZE)])
        self.Y = np.array([self.f(i) for i in self.X])

    def optimize(self, evalationNum):
        pass

    def __init__(self, f):
        self.eval = 0
        self.f = f
        self.__sampling(1)
        self.model = FuzzyCM(self.X, self.Y)
        self.__print()


if __name__ == "__main__":

    # test function
    def f(x: float):
        sum = np.sum(x)
        return np.sin(np.sqrt(sum)*10.0)

    print("--- start ---")
    ego = EGO(f)
    print("-- optimize --")
    ego.optimize(30)
    print("--- finish ---")
