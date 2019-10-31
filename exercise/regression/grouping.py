
from lbfr import Model
from pyDOE import lhs
import numpy as np
import sys

sys.path.append("./../../")
import eval
import function


def nextIt(val, dim, mxDim, frm, mxFrm):
    newV = val + [frm]
    if dim == mxDim:
        return newV

    ar = [newV]
    ar = [newV] + [nextIt(newV, dim+1, mxDim, i, mxFrm)
                   for i in range(frm, mxFrm)]

    if dim < mxDim - 1:
        p = [ar[0]]
        for l in ar[1:]:
            p += l
        return p

    return ar


def setIt(w, dim, wDim):
    it = [nextIt([], 1, wDim, frm, dim) for frm in range(dim)]
    it = np.hstack(it)
    return [[v, i] for v, i in zip(w, it)]


if __name__ == "__main__":
    dim = 7
    wDim = 2
    size = 100

    f = function.Rastrigin

    x = np.array([[s[i] for i in range(dim)] for s in lhs(dim, size)])
    y = np.array([f(i) for i in x])

    model = Model(x, y, wDim=wDim)
    w = model.w

    print("rmse = {}".format(eval.RMSE(dim, f, model)))

    mx = max(w)
    mn = min(w)
    w = np.array(
        list(map(lambda x: (x-mn)/(mx-mn) if mx-mn > 1e-5 else x/mx, w)))
    print(w)

    it = setIt(w, dim, wDim)
    it = sorted(it, reverse=True)

    for i in it:
        for j, t in enumerate(i[1]):
            print("x{}".format(t), end="," if j+1 < len(i[1]) else "\t")
        print("{:.4f}".format(i[0]))
