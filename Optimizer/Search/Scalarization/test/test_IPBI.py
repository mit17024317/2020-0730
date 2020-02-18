import os
import sys

import numpy as np
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
module = __import__("Scalarization", fromlist=["IPBI"])


class TestIPBI:
    @pytest.mark.parametrize(
        ("x", "w", "ans"),
        [
            (np.array([0.4, 0.2]), np.array([0.6, 0.8]), 0.4),
            (np.array([1.0, 1.0]), np.array([0.6, 0.8]), 1.4),
        ],
    )
    def test_f_0(self, x: np.ndarray, w: np.ndarray, ans: float) -> None:
        ipbi = module.IPBI.IPBI(0.0)
        val = ipbi.f(x, w)
        assert np.abs(val + ans) < 1e-5

    @pytest.mark.parametrize(
        ("x", "w"),
        [
            (np.array([0.4, 0.2]), np.array([0.6, 0.8])),
            (np.array([1.0, 1.0, 0.1, 0.1]), np.array([0.1, 0.4, 0.5, 0.7])),
        ],
    )
    def test_f_all(self, x: np.ndarray, w: np.ndarray) -> None:
        ipbi0 = module.IPBI.IPBI(0.0)
        d1 = -ipbi0.f(x, w)
        for p in range(1, 10):
            newX = np.array([1.0 - t for t in x])
            d2 = np.linalg.norm(newX - d1 * w)
            ipbi = module.IPBI.IPBI(p)
            val = ipbi.f(x, w)
            assert np.abs(val + d1 + d2 * p) < 1e-5
