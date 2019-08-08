import pytest
from eval import RMSE
from testModel import testFunc, testModel


@pytest.mark.parametrize(("dim"), [
#    (1), (2), (10), (50), (100)
    (3)
])
def test_RMSE(dim):
    rmse = RMSE(dim, testFunc, testModel)
    assert rmse == 5*10000
