#!/usr/bin/env python3
from model import FuzzyCM
from model import GroupingModel


class WeightModel:
    def __init__(self, model):
        self.model = model
        self.weight = 0.0


class SelectModel:
    def __init__(self, models):
        self.models = [WeightModel(m) for m in models]

    def getModel(self):
        it = self.models.index(max(self.models, key=lambda m: m.weight))
        return self.models[it].model


if __name__ == "__main__":
    sm = SelectModel([FuzzyCM, GroupingModel])
    
    print(sm.getModel())
