import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
module = __import__("Acquisition", fromlist=["EI"])


class TestEI:
    @pytest.mark.skip
    def test_f(self, mean, var, basis) -> float:
        ...
