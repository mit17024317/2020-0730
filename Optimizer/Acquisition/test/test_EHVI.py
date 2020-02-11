import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
module = __import__("Acquisition", fromlist=["EI, EHVI"])


class TestEHVI:
    @pytest.mark.skip
    def test_f(self, mean, var, pops) -> float:
        ...
