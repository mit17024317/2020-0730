import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
module = __import__("Functions", fromlist=["function"])


@pytest.mark.parametrize(("x"), [(1), (2)])
def test_original2(x):
    assert module.function.g(x) == 1
