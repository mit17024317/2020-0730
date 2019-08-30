
import matplotlib.pyplot as plt
import csv


def add(lst1, lst2):
    lst = []
    for i in range(len(lst1)):
        lst.append(lst1[i]+lst2[i])
    return lst


def toF(lst):
    return [float(t) for t in lst]


def generate(prob):
    files = ["norm", "mix"]
    for name in files:
        with open("{}/min_{}.csv".format(prob, name), "r") as f:
            reader = csv.reader(f)
            y = []
            cnt = 0
            for row in reader:
                cnt += 1
                y = toF(row[:-1]) if y == [] else add(y, toF(row[:-1]))
            x = [x+50 for x in range(len(y))]
            # y軸小数点以下3桁表示
            plt.plot(x, [t / cnt for t in y], label=name)
    plt.legend()
    plt.xlabel("number of evaluation")
    plt.ylabel("min value")
    plt.savefig("fig/{}_min.png".format(prob))
    plt.show()


if __name__ == "__main__":
    generate("Schwefel_100")
