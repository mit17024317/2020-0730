
import matplotlib.pyplot as plt
import numpy as np
import csv


def generate(prob):

    with open("{}/rmse_{}.csv".format(prob, name), "r") as f:
        reader = csv.reader(f)
        y = []
        cnt = 0
        for row in reader:
            cnt += 1
            y = toF(row[:-1]) if y == [] else add(y, toF(row[:-1]))
        x = [x+50 for x in range(len(y))]
        # y軸小数点以下3桁表示


def getY():
    ar = np.array(list(map(float, input().split(",")[:-1])))
    cnt = 1
    while(True):
        try:
            a = np.array(list(map(float, input().split(",")[:-1])))
            cnt += 1
            ar += a
        except EOFError:
            break
    ar /= cnt
    return ar


if __name__ == "__main__":
    fileName = input()
    y = getY()
    x = [t for t in range(1, len(y)+1)]

    plt.plot(x, y)
    plt.xlabel("number of generations")
    plt.ylabel("rmse")
    plt.savefig("fig/{}_rmse.png".format(fileName))
    plt.show()
