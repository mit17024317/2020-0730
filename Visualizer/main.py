#!/usr/bin/env python3
"""visualizer main script"""

__author__ = "R.Nakata"
__date__ = "2020/02/17"

import sys
from logging import DEBUG, basicConfig, getLogger

import numpy as np

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

    # data parse
    p = Parser()
    data: np.ndarray = p.parse(filename, 30)
    print(data)
