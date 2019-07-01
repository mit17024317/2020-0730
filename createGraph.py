import numpy as np
import matplotlib.pyplot as plt

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

    plt.savefig("./fig.png")
    

# TODO
def plot3D(f):
    # create sample point for debug
    X = np.linspace(0.0, 1.0, 500)[:, None]
    Y = [f(x) for x in X]

    print("-- create figure-- ")

    # create model figure
    plt.plot(X, Y, c="r", label='function')
    plt.legend()

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.savefig("./fig.png")
    

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
