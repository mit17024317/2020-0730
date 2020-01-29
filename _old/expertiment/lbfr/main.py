
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from pyDOE import lhs
import matplotlib.pyplot as plt
import random

from models.LBFR import LBFR
from models.BF.basisFunction import *
from models.BF.bfvGenerator import *

from models.model import FuzzyCM

from functions.function import *
from functions.createGraph import *

from models.eval import *


def plot_con(f, w, v):

    x = np.arange(0, 1, 0.01) # x軸
    y = np.arange(0, 1, 0.01) # y軸

    X, Y = np.meshgrid(x, y)
    t = np.array([[a,b] for a,b in zip(X,Y)])
    Z = [f(p) for p in t]

    plt.pcolormesh(X, Y, Z, cmap='seismic') # 等高線図の生成。cmapで色付けの規則を指定する。
#plt.pcolor(X, Y, Z, cmap='hsv') # 等高線図の生成。cmapで色付けの規則を指定する。

    pp=plt.colorbar (orientation="vertical") # カラーバーの表示
    plt.savefig("functions/graph/con.png")

    x = [t[0] for t in v]
    y = [t[1] for t in v]
    s = [np.abs(t)*+1 for t in w]
    mx = np.max(s)
    mn = np.min(s)
    s = [500*(t-mn)/(mx-mn)+1 for t in s]
    plt.scatter(x,y,c="g",s=s)
    plt.savefig("functions/graph/con2.png")

    plot(f, 2)



if __name__ == "__main__":
    # parameters
    dim = 2
    div = 3
    size = 200

    # test function
    def f(x):
        return (x[0]-0.5)**2 + (x[1]-0.5)**2 
        # return (x[0]+0.25)**2 

    f = Rastrigin


    # sample point 
    x = np.array([[s[i] for i in range(dim)] for s in lhs(dim, size)])
    y = np.array([f(i) for i in x])

    # basis function vector
    bfv = BasisFunctionVector()
    bfv.add(QuadraticFunction(dim=dim, div=div).getBFV())

    # generate model
    model = LBFR(x, y, bfv)
    w = model.w

    print("RMSE = ", RMSE(2,f,model))
    t  = FuzzyCM(x,y)
    print("RMSE = ", RMSE(2,f,t))


    # output
    print(w)

    plot_con(f, w, QuadraticFunction(dim=dim, div=div).centerPoint)
    
