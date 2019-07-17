
import matplotlib.pyplot as plt
import csv


def add(lst1, lst2):
    for i in range(len(lst1)):
        lst1[i].append(lst2[i][0])
    return lst1


def toS(lst):
    return [[t.strip()] for t in lst]


def modelNum(lst):
    l = len(lst[0])
    ans = []
    for m in lst:
        v = 0
        for x in m:
            v += 1 if x == "FuzzyCM" else 0
        v /= l
        ans.append(v)
    return ans


if __name__ == "__main__":
    files = ["Norm", "Group", "mix"]
    for name in files:
        with open("{}.txt".format(name), "r") as f:
            reader = csv.reader(f)
            y = []
            for row in reader:
                y = toS(row[:-1]) if y == [] else add(y, toS(row[:-1]))
            x = [x+50 for x in range(len(y))]
            # y軸小数点以下3桁表示
            plt.plot(x, modelNum(y), label=name)
    plt.legend()
    plt.xlabel("number of evaluation")
    plt.ylabel("model")
    plt.savefig("model.png")
    plt.show()
