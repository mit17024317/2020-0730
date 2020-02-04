import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
module = __import__("Functions", fromlist=["FunctionSelector"])


@pytest.mark.skip
def test_selectFunction(name: str) -> None:
    ...
