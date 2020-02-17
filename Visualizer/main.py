#!/usr/bin/env python3
"""visualizer main script"""

__author__ = "R.Nakata"
__date__ = "2020/02/17"

import sys
from logging import DEBUG, basicConfig, getLogger

import cson
import numpy as np

from graph.Hypervolume import HypervolumeVisualizer
from Parser import Parser

logger = getLogger(__name__)
args = sys.argv

if __name__ == "__main__":
    formatter = "%(levelname)s: %(message)s"
    basicConfig(level=DEBUG, format=formatter)

    # parameter check
    if len(args) < 2:
        logger.critical(
            "Need Input Parameters! You should add filename to command line."
        )
        sys.exit(1)
    filename: str = args[1]

    with open("Visualizer/param.cson", "r") as f:
        param = cson.load(f)
        hv: HypervolumeVisualizer = HypervolumeVisualizer(5)
        for d in param["data"]:
            # data parse
            p: Parser = Parser()
            dataAll: np.ndarray = p.parse(d["filename"], 30)
            data: np.ndarray = dataAll[d["itr"]]
            hv.addToPlt(data, d["name"])
        hv.saveAndShow("sample.png")