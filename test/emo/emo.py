#!/usr/bin/env python3
from platypus import MOEAD
from platypus.indicators import Hypervolume
from platypus.problems import DTLZ2


if __name__ == "__main__":

    problem = DTLZ2(3)

    hv = Hypervolume(minimum=[0,0,0], maximum=[1,1,1])
    for i in range(1,6):
        print("-- ", i, "th run --")
        algorithm = MOEAD(problem)
        algorithm.run(200)
        print(hv(algorithm.result))


