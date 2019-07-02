#!/usr/bin/env python3

import numpy as np
from pyDOE import lhs
import matplotlib.pyplot as plt
from model import FuzzyCM
from model import GroupingModel
import function as fc
from eval import RMSE

if __name__ == "__main__":
    fl = [fc.Schwefel, fc.Rosenbrock, fc.Rastrigin]
    ml = [FuzzyCM, GroupingModel]
    cll = [["normal", "black"], ["Group", "red"]]
    SIZE = 500
    cnt = 0
    for f in fl:
        sampleX = [i for i in range(1, 50)]
        for m, cl in zip(ml, cll):
            sampleY = []
            for DIM in sampleX:

                # create sample point
                X = np.array([[s[i] for i in range(DIM)] for s in lhs(DIM, SIZE)])
                Y = np.array([f(i) for i in X]) 
                model = m(X, Y)
                
                # calc RMSE
                val = RMSE(DIM, f, model)
                sampleY.append(val)
                print("dim= ", DIM, ": ", val)
            
            plt.plot(sampleX, sampleY, marker=".", markersize=10, label=cl[0], c=cl[1])
            plt.legend()

            plt.xlabel("dimension")
            plt.ylabel("RMSE")

        cnt += 1
        plt.savefig("./ex/rmse_dim_{}.png".format(cnt))
        plt.close()
