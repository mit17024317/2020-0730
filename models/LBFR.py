#!/usr/bin/env python3
"""Linear Basis Function Model."""

import numpy as np
from pyDOE import lhs

__author__ = "R.Nakata"
__date__ = "2019/11/01"

class BasisFunction():
    """
    basis function class

    attributes
    ----------
    f : function
        basis function
    """

    def __init__(self, f):
        """
        parameters
        ----------
        f : function
            basis function
        """
        self.__f = f

    def f(self, x: list):
        """
        get f value

        Parameters
        ----------
        x : list
            design variable
        """
        return self.__f(x)


class BasisFunctionVector():
    """
    basis function list

    attributes
    ----------
    bfv : list
        basis function vector
    """

    def __init__(self):
        """
        """
        self.__bfv = []

    def add(self, bf: BasisFunction):
        """
        add bf to basis function vector

        parameters
        ----------
        bf : BasisFunction
            new basis function
        """
        self.__bfv.append(bf)

    def f(self, x: list):
        """
        get all f value

        Parameters
        ----------
        x : list
            design variable

        Returns
        -------
        fv : list
            f value vector
        """
        fv = [bf.f(x) for bf in self.__bfv]
        return fv


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
