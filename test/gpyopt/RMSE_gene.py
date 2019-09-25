import sys
import random
import csv
import GPy

import numpy as np
from gpyopt import f as func

from pyDOE import lhs


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
        sum += (func(np.array([data])) -
                model.predict(np.array([data]))[0][0][0])**2
    rmse = np.sqrt(sum/size)

    return rmse


# RMSE dataset
RMSE.max = 101
RMSE.dataset = [[] for i in range(RMSE.max+1)]


def gpr(x):
    dim = len(x[0])
    kernel = GPy.kern.RBF(dim)+GPy.kern.Matern32(dim)

    y = np.array([func(np.array([t])) for t in x])

    model = GPy.models.GPRegression(x, y[:, None], kernel=kernel)
    model.optimize()

    return model


def run():

    x = []
    with open("./data/eval.txt") as f:
        reader = csv.reader(f, delimiter='\t')
        _ = next(reader)
        for r in reader:
            d = list(map(float, r[2:]))
            x.append(np.array(d))
    x = np.array(x)

    dim = len(x[0])
    for i in range(1, len(x)):
        model = gpr(x[0:i])
        print(RMSE(dim, func, model))


if __name__ == "__main__":
    run()
