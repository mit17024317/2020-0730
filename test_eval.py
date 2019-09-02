import pytest
from eval import RMSE, RMSE_G, RMSE_P
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
