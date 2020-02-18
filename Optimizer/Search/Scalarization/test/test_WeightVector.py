import os
import sys

import numpy as np
import pytest
from scipy.special import comb

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
module = __import__("Scalarization", fromlist=["WeightVector"])


class TestRandomWeight:
    @pytest.mark.parametrize(
        ("dim", "division"), [(3, 3), (1, 10), (5, 5), (2, 15)],
    )
    def test_generateWeightList(self, dim, division) -> None:
        rw = module.WeightVector.RandomWeight()
        wvl = rw.generateWeightList(dim, division)
        for wv in wvl:
            assert len(wv) == dim
            s = np.sqrt(np.sum(np.frompyfunc(lambda x: x * x, 1, 1)(wv)))
            assert np.abs(s - 1.0) < 1e-5
        assert len(wvl) == division


class TestUniformalWeight:
    @pytest.mark.parametrize(
        ("dim", "division"), [(3, 3), (1, 10), (5, 5), (2, 15)],
    )
    def test_generateWeightList(self, dim, division) -> None:
        rw = module.WeightVector.UniformalWeight()
        wvl = rw.generateWeightList(dim, division)
        for wv in wvl:
            assert len(wv) == dim
            s = np.sqrt(np.sum(np.frompyfunc(lambda x: x * x, 1, 1)(wv)))
            assert np.abs(s - 1.0) < 1e-5
        assert len(wvl) == comb(division + dim - 1, dim - 1, exact=True)
