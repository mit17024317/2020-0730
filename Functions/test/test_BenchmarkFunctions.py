import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
module = __import__("Functions", fromlist=["BenchmarkFunctions"])


class TestRosenbrock:
    @pytest.mark.skip
    def test_f(self, x):
        ...


class TestRastrigin:
    @pytest.mark.skip
    def test_f(self, x):
        ...


class TestSchwefel:
    @pytest.mark.skip
    def test_f(self, x):
        ...
