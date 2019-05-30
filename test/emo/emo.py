#!/usr/bin/env python3
from platypus import MOEAD, Problem, Real


def schaffer(x):
    return [x[0]**2, (x[0]-2)**2]


if __name__ == "__main__":
    problem = Problem(1, 2)
    problem.types[:] = Real(-10, 10)
    problem.function = schaffer

    algorithm = MOEAD(problem)
    algorithm.run(10000)
