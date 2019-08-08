
import pytest
from function import original2


@pytest.mark.parametrize(("x", "y"), [
    ([5], 6),
    ([2, 3], 5),
    ([2, 3, 4], 14),
    ([2, 3, 4, 5], 26),
    ([2, 3, 4, 5, 6], 126)
])
def test_original2(x, y):
    f = original2(x)
    assert f == y
