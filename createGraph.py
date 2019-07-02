import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def plot2D(f):
    # create sample point for debug
    X = np.linspace(0.0, 1.0, 500)[:, None]
    Y = [f(x) for x in X]

    print("-- create figure-- ")

    # create model figure
    plt.plot(X, Y, c="r", label='function')
    plt.legend()

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.savefig("./graph/2D.png")
    plt.clf()
    

def plot3D(f):
    PNUM = 100
    # create sample point for debug
    x1 = np.linspace(0.0, 1.0, PNUM)
    x2 = np.linspace(0.0, 1.0, PNUM)

    X1, X2 = np.meshgrid(x1, x2)

    Y = []
    for h in x1:
        tmp = []
        for w in x2:
            tmp.append(f([h, w]))
        Y.append(tmp)
    Y = np.array(Y)

    print("-- create figure-- ")
    # create model figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.plot_wireframe(X1, X2, Y, color="darkblue")

    plt.savefig("./graph/3D.png")
    plt.clf()
    

def plot(f, d):
    if d == 1:
        plot2D(f)
    elif d == 2:
        plot3D(f)

if __name__ == "__main__":
    # debug parameter
    DIM = 10
    SIZE = 30

    # test function
    def f(x: float):
        sum = np.sum(x)
        return np.sin(np.sqrt(sum)*10.0)

    plot(f, 1)
    plot(f, 2)
    print("--- finish ---")
