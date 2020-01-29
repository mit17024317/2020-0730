#!/usr/bin/env python3
"""Basis Function Vector generator interface."""

__author__ = "R.Nakata"
__date__ = "2019/11/01"


from abc import ABC, abstractmethod
import numpy as np
import copy

from .basisFunction import *


class BFVGeneratorInterface(ABC):
    @abstractmethod
    def getBFV(self):
        pass


class QuadraticFunction(BFVGeneratorInterface):
    """
    Quadratic Functio Vector.

    attributes
    ----------
    bfv : BasisFunctionVector
        basis function vector 
    centerPoint : list<list>
        Quadratic Function's center point
    """

    def __init__(self, dim: int, div: int = 10):
        """
        Parameters
        ----------
        dim : int
            function's dimension
        div: int
            divide num (vector size = 2*pow(div, dim))
        """
        self.centerPoint = []
        self.__bfv = self.__generate(dim, div)

    def __generate(self, dim: int, div: int):
        """
        genaraete BFV using Quadratic Function

        Parameters
        ----------
        dim : int
            function's dimension
        div: int
            divide num (vector size = 2*pow(div, dim))

        Returns
        -------
        bfv : BasisFunctionVector
            basis function vector using Quadratic Function
        """
        # moved Quadratic Function
        class MoveQuadratic:
            def __init__(self, v):
                self.dif = v
            def f(self, x:list):
                return np.sum((x-self.dif)**2)
        # add dif 
        def add(v, dif):
            j = 0
            while True:
                if np.abs(v[j]+dif-1.0) < 1e-5:
                    v[j] = dif
                    j+=1
                else:
                    v[j] += dif
                    break
            return v

        # initilize dif 
        dif = 1.0/(div+1.0)
        difV = np.array([dif for _ in range(dim)])

        # add moved quadratic
        v = copy.deepcopy(difV)
        bfv = [MoveQuadratic(v)]
        self.centerPoint.append(v)
        for _ in range(np.power(div,dim)-1):
            difV = add(difV, dif)
            v = copy.deepcopy(difV)
            bfv.append(MoveQuadratic(v))
            self.centerPoint.append(v)

        return bfv

    def getBFV(self):
        """
        get BFV

        Returns
        -------
        bfv : BasisFunctionVector
            basis function vector using Quadratic Function
        """
        return self.__bfv


if __name__ == "__main__":
    q = QuadraticFunction(dim=5, div=3)
