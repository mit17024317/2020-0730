import os
import sys

import numpy as np
import pytest
from numpy.random import normal

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
module = __import__("Acquisition", fromlist=["EI"])


class TestEI:
    @pytest.mark.parametrize(
        ("mean", "var", "base"),
        [(0.0, 1.0, 0.5), (0.8, 0.1, 0.3), (0.1, 1.3, 0.7), (0.4, 0.1, 0.3), ],
    )
    def test_f(self, mean, var, base) -> float:
        # 厳密解
        AF = module.EI.EI()
        ei = AF.f(mean, var, base)

        # 近似解(モンテカルロ積分)
        sum = 0.0
        size = 100000
        for x in normal(mean, var, size):
            sum += np.max([base - x, 0.0])
        sum /= size
        print(sum, ei)

        # 差分
        dif = np.abs(sum - ei)
        assert dif < 0.1
