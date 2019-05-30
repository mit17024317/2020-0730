#!/usr/bin/env python3
import GPy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    kernel = GPy.kern.RBF(1)
    # kernel = GPy.kern.RBF(1) + GPy.kern.Bias(1) + GPy.kern.Linear(1)

    d = pd.read_csv('http://kasugano.sakura.ne.jp/'
                    'images/2016/20161112/data-GPbook-Fig2_05.txt')
    model = GPy.models.GPRegression(d.X[:, None], d.Y[:, None], kernel=kernel)
    model.optimize()
    model.plot()
    plt.savefig('./fig.png')

    # prediction
    x_pred = np.linspace(-10, 10, 100)
    x_pred = x_pred[:, None]
    y_qua_pred = model.predict_quantiles(x_pred, quantiles=(2.5, 50, 97.5))[0]
    print("-- finish --")
