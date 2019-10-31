
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from pyDOE import lhs

from models.LBFR import LBFR
from models.BF.basisFunction import *
from models.BF.bfvGenerator import *


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
    bfv.add(QuadraticFunction(dim=dim, div=5).getBFV())

    # generate model
    model = LBFR(x, y, bfv)
    w = model.w

    # output
    print(w)

    
