import pytest
from eval import *
from testModel import testFunc, testModel


@pytest.mark.parametrize(("dim"), [
    (1), (2), (10), (50), (100)
])
def test_RMSE(dim):
    rmse = RMSE(dim, testFunc, testModel())
    assert rmse == 5


@pytest.mark.parametrize(("dim"), [
    (1), (2), (10), (50), (100)
])
def test_RMSE_G(dim):
    rmse = RMSE_G(dim, testFunc, testModel())
    assert rmse == 5


@pytest.mark.parametrize(("dim"), [
    (1), (2), (10), (50), (100)
])
def test_RMSE_P(dim):
    newIndiv = [0.0 for x in range(dim)]
    rmse = RMSE_P(dim, testFunc, testModel(), newIndiv)
    assert rmse == 5


@pytest.mark.parametrize(("idv", "nidv", "ave", "med"), [
    ([[0], [0], [0]], [1], 1, 1),
    ([[1], [2], [3], [4]], [3], 1, 1),
    ([[1, 1], [0, 1], [3, 2]], [0, 2], 4+np.sqrt(2), np.sqrt(2)),
])
def test_distanceValue(idv, nidv, ave, med):
    a, m = distanceValue(idv, nidv)
    assert a-ave < 1e-7
    assert m-med < 1e-7


def test_distanceValue_large():
    base = [0.0 for k in range(100)]
    idv = [base for _ in range(100)]
    a, m = distanceValue(idv, base)
    assert a-0.0 < 1e-7
    assert m-0.0 < 1e-7
