import os
import sys

import numpy as np
import pytest
from numpy.random import rand

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
module = __import__("Models", fromlist=["GPR"])


class TestGPR:
    @pytest.mark.skip
    def test_getPredictValue(self, x):
        ...

    @pytest.mark.skip
    def test_getPredictDistribution(self, x):
        ...

    @pytest.mark.parametrize(
        ("dim", "obj", "num"),
        [(3, 2, 10), (5, 3, 10), (10, 10, 10), (5, 5, 20), (10, 10, 50)],
    )
    def test_getPredictDistributionAll_random(self, dim, obj, num):

        x = np.array([[rand() for _ in range(dim)] for __ in range(num)])
        y = np.array([rand() for _ in range(num)])

        model = module.GPR.GPR(x, y)

        p = np.array([[rand() for _ in range(dim)] for __ in range(num)])
        mvL = model.getPredictDistributionAll(p)

        for t, mv in zip(p, mvL):
            m, v = model.getPredictDistribution(t)
            assert np.abs(m - mv[0]) < 1e-5
            assert np.abs(v - mv[1]) < 1e-5

    @pytest.mark.parametrize(
        ("dim", "obj", "num"),
        [(3, 2, 10), (5, 3, 10), (10, 10, 10), (5, 5, 20), (10, 10, 50)],
    )
    def test_getPredictValueAll_random(self, dim, obj, num):

        x = np.array([[rand() for _ in range(dim)] for __ in range(num)])
        y = np.array([rand() for _ in range(num)])

        model = module.GPR.GPR(x, y)

        p = np.array([[rand() for _ in range(dim)] for __ in range(num)])
        vL = model.getPredictValueAll(p)

        for t, v in zip(p, vL):
            v2 = model.getPredictValue(t)
            assert np.abs(v - v2) < 1e-5
