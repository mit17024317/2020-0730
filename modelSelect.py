#!/usr/bin/env python3
import numpy as np
from model import FuzzyCM
from model import GroupingModel


class WeightModel:
    def __init__(self, model, X, Y):
        self.model = model(X, Y)
        self.weight = 0.0

    def update(self, indiv, valEval, X, Y):
        print(indiv)
        val = self.model.getPredictValue(np.array([indiv]))[0]
        self.weight += val



class SelectModel:
    def __init__(self, models, X, Y):
        self.models = [WeightModel(m, X, Y) for m in models]

    def getModel(self):
        print([x.weight for x in self.models])
        it = self.models.index(max(self.models, key=lambda m: m.weight))
        return self.models[it].model

    def update(self, indiv, valEval):
        for i, _ in enumerate(self.models):
            self.models[i].update(indiv, valEval)


if __name__ == "__main__":
    sm = SelectModel([FuzzyCM, GroupingModel])
    
    print(sm.getModel())

