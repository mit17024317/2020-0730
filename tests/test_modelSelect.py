import pytest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from function_t import testModel, testFunc
from models.modelSelect import WeightRecentModel, WeightAddModel, SelectModel


class TestWeightRecentModel:
    @pytest.mark.parametrize(("indivList"), [
        ([[10]]),
        ([1], [2], [3], [4], [5], [6], [7]),
        ([[5, 3.1], [19, 0.1], [0.01, 1.3], [2.1, 6.3],
          [0.0, 0.0], [1.3, 4.1], [1.1, 1.1]])
    ])
    def test_updete(self, indivList):
        m = WeightRecentModel(testModel, None, None)
        valList = [5*x if x < 5 else 5*5 for x in range(1, len(indivList)+1)]
        for idv, val in zip(indivList, valList):
            m.update(idv, testFunc(idv), None, None)
            assert m.weight == val


class TestWeightAddModel:
    def test___init__(self):
        m = WeightAddModel(testModel, None, None)
        assert m.weight == 0

    @pytest.mark.parametrize(("indivList"), [
        ([[10]]),
        ([[5], [19], [1.3], [6.3]]),
        ([[5, 3.1], [19, 0.1], [0.01, 1.3], [2.1, 6.3]]),
    ])
    def test_updete(self, indivList):
        m = WeightAddModel(testModel, None, None)
        valList = [5*x for x in range(1, len(indivList)+1)]
        for idv, val in zip(indivList, valList):
            m.update(idv, testFunc(idv), None, None)
            assert m.weight == val


class TestSelectModel:
    @pytest.mark.parametrize(("weighter", "wList"), [
        (WeightAddModel, [[10, 10], [7, 5]]),
        (WeightAddModel, [[1, 3, 2], [2, 2, 2], [1, 3, 1], [3, 1, 3]])
    ])
    def test_getModel(self, weighter, wList):
        sm = SelectModel([testModel for _ in range(
            len(wList[0]))], None, None, weighter)

        for wl in wList:
            minItr = 0
            for i, w in enumerate(wl):
                sm.models[i].weight = w
                minItr = i if w < wl[minItr] else minItr
            assert sm.getModel() == sm.models[minItr].model
