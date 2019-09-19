import GPy
import GPyOpt
import numpy as np

import sys
import random


def RMSE(dim, func, model, size=10000):
    """
    normal RMSE

    Parameters
    ----------
    dim : int
        dimension of problem
    func : function: array:double -> double
        True Function
    model : ModelInterface
        func's model
    size : int
        point of rmse size

    Returns
    -------
    rmse : double
        rmse value of model
    """
    if dim > RMSE.max:
        print("!! eval.py RMSE error !!")
        print("update RMSE.max greater than ", dim)
        sys.exit()
    if RMSE.dataset[dim] == []:
        RMSE.dataset[dim] = \
            np.array([[random.random() for k in range(dim)]
                      for i in range(size)])

    sum = 0.0
    for data in RMSE.dataset[dim]:
        sum += (func(np.array([data]))-model.predict(np.array([data]))[0][0][0])**2
    rmse = np.sqrt(sum/size)

    return rmse


# RMSE dataset
RMSE.max = 101
RMSE.dataset = [[] for i in range(RMSE.max+1)]


def f(x):
    lst = x[:, 0]**2
    for i in range(1, len(x[0])):
        lst += x[:, i]**2
    return np.sum(lst)/50

def g(x):
    return np.cos(1.5*x) + 0.1*x

if __name__ == "__main__":
    bounds = [
        {'name': 'x{}'.format(x), 'type': 'continuous', 'domain': (-1, 1)}
        for x in range(1)
    ]
    myBopt = GPyOpt.methods.BayesianOptimization(
        f=g, domain=bounds, initial_design_numdata=5, acquisition_type='EI')

    myBopt.run_optimization(max_iter=1)
    print(RMSE(1, f, myBopt.model))
    for _ in range(50):
        myBopt.run_optimization(max_iter=10)
        print(RMSE(1, f, myBopt.model))

    print(myBopt.fx_opt)
