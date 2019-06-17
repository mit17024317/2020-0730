#!/usr/bin/env python3
from abc import ABC, abstractmethod
import GPy
import numpy as np
from skfuzzy.cluster import cmeans
import matplotlib.pyplot as plt
from pyDOE import lhs
import time
import random

class modelInterface(ABC):
    @abstractmethod
    def getPredictValue(self, x: list):
        pass
    @abstractmethod
    def getPredict(self, x: float):
        pass

class GPR(modelInterface):

    def __init__(self, sampleX: list, sampleY: list):
        DIM = sampleX[0].size
        kernel = GPy.kern.RBF(DIM)+GPy.kern.Matern32(DIM)
        self.model = GPy.models.GPRegression(sampleX, sampleY[:, None], kernel=kernel)
        self.model.optimize()

    def getPredictValue(self, x: list, a=2.5, b=50, c=97.5):
        return [val[0] for val in
                self.model.predict_quantiles(
                    x,
                    quantiles=(a, b, c)
                )[1]]

    def getPredict(self, x: float):
        return self.model.predict(np.array([x]))



class FuzzyCM(modelInterface):

    def __init__(self, sampleX: list, sampleY: list):
        # clusterMaxSize
        N = min(100, len(sampleX))
        clusterNum = 1 if N < 50 else 1 + int(len(sampleX) / (N - 10))
        DIM = sampleX[0].size

        # data, m, c, error, maxIter, init, seed
        # center, result, firstResult, distance?, ?, loopNum, ?
        self.models = []
        cntr, u, u0, d, jm, p, fpc = cmeans(sampleX.T, clusterNum, 3.0,  0.01, 1000)
        for c, x in zip(cntr, u):
            kernel = GPy.kern.RBF(DIM)+GPy.kern.Matern32(DIM)
            arg = np.argsort(x)[::-1]
            X = np.array([sampleX[t] for t in arg[:N]])
            Y = np.array([sampleY[t] for t in arg[:N]])
            mdl = GPy.models.GPRegression(X, Y[:, None], kernel=kernel)
            mdl.optimize()
            self.models.append({"m": mdl, "c": c})

    def __getCloseCenter(self, x: list):
        itr = 0
        min = 1e100
        for i, mdl in enumerate(self.models):
            cntr = mdl["c"]
            dis = np.linalg.norm(cntr-x)
            if dis < min:
                min = dis
                itr = i
        return itr

    def getPredictValue(self, x: list, a=2.5, b=50, c=97.5):
        all = [[val[0] for val in
                self.models[itr]["m"].predict_quantiles(
                    x,
                    quantiles=(a, b, c)
                )[1]]
               for itr in range(len(self.models))]
        val = [all[self.__getCloseCenter(x[i])][i] for i in range(len(x))]
        return val

    def getPredict(self, x: float):
        return self.models[self.__getCloseCenter(x)]['m'].predict(np.array([x]))


class GroupingModel(modelInterface):

    def __init__(self, sampleX: list, sampleY: list):
        self.models = []
        self.__createGroupModel(sampleX, sampleY)

    def __createGroupModel(self, sampleX: list, sampleY: list):
        group = self.__grouping(len(sampleX[0]))
        size = len(sampleX)
        GsampleX = [[[sampleX[i][p]
                    for p in g]
                    for i in range(size)]
                    for g in group]
        self.models = [FuzzyCM(np.array(GsampleX[g]), sampleY) for g in range(len(group))]

    def __grouping(self, size):
        lst = random.sample([x for x in range(size)], size)
        if size < 5:
            return [np.array(lst)]
        size = (len(lst)+4)/5
        lst = np.array_split(lst, size)
        return lst

    def getPredictValue(self, x: list, a=2.5, b=50, c=97.5):
        sum = np.array([0.0 for i in range(len(x))])
        for model in self.models:
            sum += np.array(model.getPredictValue(x))
        return list(sum/len(self.models))

    def getPredict(self, x: float):
        sum = np.array([0.0 for i in range(len(x))])
        for model in self.models:
            sum += np.array(model.getPredict(x))
        return list(sum/len(self.models))


if __name__ == "__main__":
    # debug parameter
    DIM = 10
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
    s1 = time.time()
    # MODEL = GPR(X, Y)
    s2 = time.time()
    # MODEL_FUZZY = FuzzyCM(X, Y)
    s3 = time.time()
    MODEL_GROUP = GroupingModel(X, Y)
    s4 = time.time()
    print("GPR:\t{0}ms".format(1000*(s2-s1)),
          "FuzzyCM:\t{0}ms".format(1000*(s3-s2)),
          "Group:\t{0}ms".format(1000*(s4-s3)), sep="\n")

    if DIM == 1:
        # create sample point for debug
        ALL_X = np.linspace(0.0, 1.0, 500)[:, None]
        ALL_Y_TRUE = [f(x) for x in ALL_X]
        # ALL_Y_GPR = MODEL.getPredictValue(ALL_X)
        # ALL_Y_FUZZY = MODEL_FUZZY.getPredictValue(ALL_X)
        ALL_Y_GROUP = MODEL_GROUP.getPredictValue(ALL_X)

        print("-- create figure-- ")
        # create model figure
        plt.plot(ALL_X, ALL_Y_TRUE, c="r", label='function')
        # plt.plot(ALL_X, ALL_Y_GPR, c="b", label='GPR')
        # plt.plot(ALL_X, ALL_Y_FUZZY, c="y", label='Fuzzy CM')
        plt.plot(ALL_X, ALL_Y_GROUP, c="g", label='Grouping Model')
        plt.plot(X, Y, 'o', marker=".", markersize=10, c="black", label="sample point")
        plt.legend()

        plt.xlabel("X")
        plt.ylabel("Y")

        plt.savefig("./fig.png")
    print("--- finish ---")
