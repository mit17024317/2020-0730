#!/usr/bin/env python3
"""Linear Basis Function Model."""

import numpy as np

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
        if type(bf) is list:
            self.__bfv += bf
        else:
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


if __name__ == "__main__":
    # basis function vector
    bfv = BasisFunctionVector()
    bfv.add(BasisFunction(lambda x: x[0]*x[1]))
    bfv.add(BasisFunction(lambda x: x[0]*x[0]))
    bfv.add(BasisFunction(lambda x: x[1]*x[1]))
    bfv.add(BasisFunction(lambda x: x[0]))
    bfv.add(BasisFunction(lambda x: x[1]))

    # point
    p = np.array([5, 4])
    print(bfv.f(p))
    p = np.array([1, 2])
    print(bfv.f(p))
