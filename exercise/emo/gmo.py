#!/usr/bin/env python3
from platypus.problems import DTLZ2
from platypus.core import Solution

if __name__ == "__main__":
    problem = DTLZ2(1)

    s = Solution(problem)
    s.variables = [0.3]
    s.evaluate()

    print(s)
