
from lbfr import Model
from pyDOE import lhs
import numpy as np
import sys

sys.path.append("./../../")
import function
import eval


if __name__ == "__main__":
    dim = 2
    wDim = 2
    size = 100

    f = function.easyFunc
    f = lambda x:x[0]*x[1]

    x = np.array([[s[i] for i in range(dim)] for s in lhs(dim, size)])
    y = np.array([f(i) for i in x])

    model = Model(x, y, wDim=wDim)
    w = model.w
    
    print(w)
    print("rmse = {}".format(eval.RMSE(dim, f, model)))
