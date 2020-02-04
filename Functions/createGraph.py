# REVIEW: 関数を多目的対応させたので調整が必要
# HACK: 必要になった場合にドキュメント等を追加

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d


def plot2D(f, s=False):
    # create sample point for debug
    X = np.linspace(0.0, 1.0, 500)[:, None]
    Y = [f(x) for x in X]

    print("-- create figure-- ")

    # create model figure
    plt.plot(X, Y, c="r", label="function")
    plt.legend()

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.savefig("./functions/graph/2D.png")
    if s:
        plt.show()
    plt.close()


def plot3D(f, s=False):
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

    plt.savefig("./functions/graph/3D.png")
    if s:
        plt.show()
    plt.close()


def plot(f, d, s=False):
    if d == 1:
        plot2D(f, s)
    elif d == 2:
        plot3D(f, s)


if __name__ == "__main__":
    # debug parameter
    DIM = 10
    SIZE = 30

    # test function
    def f(x):
        sum = np.sum(x)
        return np.sin(np.sqrt(sum) * 10.0)

    plot(f, 1)
    plot(f, 2, True)
    print("--- finish ---")
