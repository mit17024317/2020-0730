#!/usr/bin/env python3
import numpy as np
from pyDOE import lhs

from models.model import FuzzyCM, GroupingModel

class WeightRecentModel:
    def __init__(self, model, X, Y):
        self.modelClass = model
        self.model = model(X, Y)
        self.weight = 0.0
        self.weightList = []

    def update(self, indiv, valEval, X, Y):
        val = self.model.getPredict(np.array(indiv))[0]
        self.weightList.append(abs(valEval - val))
        self.weight += self.weightList[-1]
        if len(self.weightList) > 5:
            self.weight -= self.weightList[0]
            self.weightList = self.weightList[1:]
        self.model = self.modelClass(X, Y)


class WeightAddModel:
    def __init__(self, model, X, Y):
        self.modelClass = model
        self.model = model(X, Y)
        self.weight = 0.0

    def update(self, indiv, valEval, X, Y):
        val = self.model.getPredict(np.array(indiv))[0]
        self.weight += abs(valEval - val)
        self.model = self.modelClass(X, Y)


class SelectModel:
    def __init__(self, models, X, Y, weighter=WeightAddModel):
        self.models = [weighter(m, X, Y) for m in models]

    def getModel(self):
        it = self.models.index(min(self.models, key=lambda m: m.weight))
        return self.models[it].model

    def update(self, indiv, valEval, X, Y):
        for i, _ in enumerate(self.models):
            self.models[i].update(indiv, valEval, X, Y)


if __name__ == "__main__":
    # debug parameter
    DIM = 10
    SIZE = 30

    # test function
    def f(x: float):
        sum = np.sum(x)
        return np.sin(np.sqrt(sum)*10.0)

    # create sample point
    X = np.array([[s[i] for i in range(DIM)] for s in lhs(DIM, SIZE)])
    Y = np.array([f(i) for i in X])

    sm = SelectModel([FuzzyCM, GroupingModel], X, Y)

    print(sm.getModel())
