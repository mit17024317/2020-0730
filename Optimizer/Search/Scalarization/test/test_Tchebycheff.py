import os
import sys

import numpy as np
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
module = __import__("Scalarization", fromlist=["Tchebycheff"])


class TestTchebycheff:
    @pytest.mark.parametrize(
        ("x", "w", "ans"),
        [
            (np.array([1, 2, 3]), np.array([0.2, 0.3, 0.5]), 1.5),
            (np.array([1, 2, 3]), np.array([0.0, 0.0, 1.0]), 3.0),
            (np.array([0.2, 0.3]), np.array([0.3, 0.2]), 0.06),
            (np.array([1]), np.array([1.0]), 1.0),
        ],
    )
    def test_f(self, x: np.ndarray, w: np.ndarray, ans: float) -> None:
        tc = module.Tchebycheff.Tchebycheff()
        val = tc.f(x, w)
        assert val == ans
