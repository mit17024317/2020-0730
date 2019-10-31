#!/usr/bin/env python3
"""Linear Basis Function Model."""

import numpy as np
from pyDOE import lhs

from .BF.basisFunction import *

__author__ = "R.Nakata"
__date__ = "2019/11/01"


class LBFR():
    """
    linear basis function regression model

    attributes
    ----------
    bfv : list
        basis function vector
    w : list
        weight vector 
    """
    def __init__(self, X:list, Y:list, bfv:list):
        """
        Parameters
        ----------
        X : list
            design variables of sample point
        Y : list
            evaluation values of sample point
        bfv: list
            basis function vector
        """
        self.bfv = bfv
        self.w = self.__calcWeight(X, Y)

    def __calcWeight(self, X:list, Y:list):
        """
        calcrate weight vector

        Parameters
        ----------
        X : list
            design variables of sample point
        Y : list
            evaluation values of sample point

        Returns
        -------
        wv :list
            weight vector
        """
        phi = np.array([self.bfv.f(x) for x in X])
        wv = np.dot(np.dot(
            np.linalg.inv(np.dot(phi.T, phi)) + np.identity(len(phi[0]))*1e-9,
            phi.T),
            Y)
        return wv

    def getPredict(self, x:list):
        """
        get predict value

        Parameters
        ----------
        x : list
            design variables

        Returns
        -------
        val : float
            predict value
        """
        val = [np.sum(self.w*self.bv.get(x)), 0.0]
        return val


if __name__ == "__main__":
    # parameters
    dim = 2
    size = 50

    # test function
    def f(x):
        return x[0] * x[1] + x[0] + x[1]

    # sample point 
    x = np.array([[s[i] for i in range(dim)] for s in lhs(dim, size)])
    y = np.array([f(i) for i in x])

    # basis function vector
    bfv = BasisFunctionVector()
    bfv.add(BasisFunction(lambda x: x[0]*x[1]))
    bfv.add(BasisFunction(lambda x: x[0]*x[0]))
    bfv.add(BasisFunction(lambda x: x[1]*x[1]))
    bfv.add(BasisFunction(lambda x: x[0]))
    bfv.add(BasisFunction(lambda x: x[1]))

    # generate model
    model = LBFR(x, y, bfv)
    w = model.w

    # output
    print(w)
