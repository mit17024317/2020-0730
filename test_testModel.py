
import numpy as np
import pytest
from testModel import testFunc
from testModel import testModel


@pytest.fixture()
def model():
    return testModel()


class TestTestModel():

    @pytest.mark.skip
    def test_getPredictValue(self, model, x, val):
        pass

    @pytest.mark.parametrize(("x", "val"), [
        ([5], 30),
        ([1, 2], 10),
        (np.array([3, -4]), 30),
        (np.array([1.2, 0.1]), 6.45)
    ])
    def test_getPredict(self, model, x, val):
        assert model.getPredict(x)[0] == val


@pytest.mark.parametrize(("x", "val"), [
    ([5], 25),
    ([-1, 1], 2),
    (np.array([10, -4, 3]), 125),
    (np.array([1.2, 0.1]), 1.45)
])
def test_testFunc(x, val):
    assert testFunc(x) == val
