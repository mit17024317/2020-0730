import GPy
import GPyOpt
import numpy as np


def f(x):
    lst = x[:, 0]**2
    for i in range(1, len(x[0])):
        lst += x[:, i]**2
    return np.sum(lst)/len(x[0])


def run():

    # parametes
    dim = 4

    # set designvariables
    bounds = [
        {'name': 'x{}'.format(x), 'type': 'continuous', 'domain': (-1, 1)}
        for x in range(dim)
    ]

    # set optimizer
    my = GPyOpt.methods.BayesianOptimization(
        f=f, domain=bounds, initial_design_numdata=5, acquisition_type='EI')

    # optimize
    my.run_optimization(max_iter=50,
                        evaluations_file="./data/eval.txt",
                        models_file="./data/model.txt",
                        report_file="./data/rep.txt",
                        )


if __name__ == "__main__":
    run()
