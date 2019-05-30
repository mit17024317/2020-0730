#!/usr/bin/env python3
import GPy
import numpy as np
import matplotlib.pyplot as plt
from pyDOE import lhs


def f(x):
    return x-np.cos(x)


if __name__ == "__main__":

    kernel = GPy.kern.RBF(1)
    # kernel = GPy.kern.RBF(1) + GPy.kern.Bias(1) + GPy.kern.Linear(1)

    x = np.array([s[0] for s in lhs(1, 3, "c")])
    y = np.array([f(i) for i in x])
    print(x, y, end='\n')

    model = GPy.models.GPRegression(x[:, None], y[:, None], kernel=kernel)
    model.optimize()
    model.plot()
    plt.savefig('./fig.png')

    # prediction
    x_pred = np.linspace(-10, 10, 100)
    x_pred = x_pred[:, None]
    y_qua_pred = model.predict_quantiles(x_pred, quantiles=(2.5, 50, 97.5))[0]
    print("-- finish --")
