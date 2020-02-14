import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
module = __import__("Models", fromlist=["GPR"])


class TestGPR:
    @pytest.mark.skip
    def test_getPredictValue(self, x):
        ...

    @pytest.mark.skip
    def test_getPredictDistribution(self, x):
        ...
