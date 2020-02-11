import os
import sys

import numpy as np
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
module = __import__("Acquisition", fromlist=["EI", "EHVI"])


class TestEHVI:
    @pytest.mark.parametrize(
        ("mean", "var", "pops"),
        [
            (np.array([0.4]), np.array([1.0]), [np.array([0.5])]),
            (np.array([0]), np.array([1]), [np.array([0.8]), np.array([0.1])]),
            (np.array([0.3]), np.array([0.2]), [np.array([0.2])]),
            (np.array([0.5]), np.array([1.3]), [
             np.array([0.6]), np.array([0.7])]),
        ],
    )
    def test_f_1dim(self, mean, var, pops) -> float:
        AF = module.EI.EI()
        ei = AF.f(mean[0], var[0], np.min(pops))
        AFM = module.EHVI.EHVI()
        ehvi = AFM.f(mean, var, pops)
        dif = np.abs(ei - ehvi)
        assert dif < 0.1

    @pytest.mark.parametrize(
        ("mean", "var", "pops"),
        [
            (np.array([0]), np.array([1]), [np.array([0.5])]),
            (
                np.array([0, 0]),
                np.array([1, 1]),
                [np.array(l) for l in [[0.3, 0.2], [0.1, 0.8]]],
            ),
            (
                np.array([0.2, 0, 0.3]),
                np.array([10, 0.1, 0.8]),
                [
                    np.array(l)
                    for l in [
                        [0.11, 0.3, 0.2],
                        [0.3123, 0.1, 0.8],
                        [0.3123, 0.1, 0.8],
                        [0.3123, 0.1, 0.8],
                        [0.3123, 0.1, 0.8],
                        [0.3123, 0.1, 0.8],
                    ]
                ],
            ),
        ],
    )
    def test_f_nonError(self, mean, var, pops) -> float:
        AFM = module.EHVI.EHVI()
        ehvi = AFM.f(mean, var, pops)
        print(ehvi)
