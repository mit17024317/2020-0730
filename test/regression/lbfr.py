
import numpy as np
from pyDOE import lhs


class BasisVector():

    def __init__(self, dim):
        self.dim = dim

    def __addX(self, x, val, dim, frm):
        val = val*x[frm]
        ar = np.array([val])
        if dim == self.dim:
            return ar

        ar = np.append(ar, [self.__addX(x, val, dim+1, i) for i in range(frm+1, len(x))])
        return np.hstack(ar)


    def get(self, x):
        self.dim = min(len(x), self.dim)
        ar = [self.__addX(x, 1, 1, frm) for frm in range(len(x))]
        return np.hstack(ar)


class Model():
    def __init__(self, X, Y, wDim = 2):
        self.bv = BasisVector(wDim)
        self.w = self.__calcWeight(X, Y)

    def __calcWeight(self, X, Y):
        phi = np.array([self.bv.get(x) for x in X])
        return np.dot(np.dot(
            np.linalg.inv(np.dot(phi.T, phi)),
            phi.T),
            Y)

    def getPredict(self, x):
        return [np.sum(self.w*self.bv.get(x)), 0.0]


if __name__ == "__main__":
    dim = 10
    size = 50

    def f(x):
        return x[0] * x[1] + x[0] + x[1]

    x = np.array([[s[i] for i in range(dim)] for s in lhs(dim, size)])
    y = np.array([f(i) for i in x])

    model = Model(x, y, wDim = 3)
    w = model.w
