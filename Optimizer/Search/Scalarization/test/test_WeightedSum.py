import os
import sys

import numpy as np
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
module = __import__("Scalarization", fromlist=["WeightedSum"])


class TestWeightedSum:
    @pytest.mark.parametrize(
        ("x", "w", "ans"),
        [
            (np.array([1, 2, 3]), np.array([0.2, 0.3, 0.5]), 2.3),
            (np.array([1, 2, 3]), np.array([0.0, 0.0, 1.0]), 3.0),
            (np.array([1]), np.array([1.0]), 1.0),
        ],
    )
    def test_f(self, x: np.ndarray, w: np.ndarray, ans: float) -> None:
        ws = module.WeightedSum.WeightedSum()
        val = ws.f(x, w)
        assert val == ans
