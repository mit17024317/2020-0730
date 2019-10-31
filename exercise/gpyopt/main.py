
import sys
import gpyopt
import RMSE_gene


def input2():
    while True:
        val = input()
        if not "#" in val and len(val) > 0 and not val[0] == ' ':
            return val


if __name__ == "__main__":

    # parameters
    title = input2()
    dim = int(input2())
    itr = int(input2())
    init = int(input2())
    num = int(input2())

    # run
    print(title)
    for i in range(1, num+1):
        print("-- {}th run-- ".format(i), file=sys.stderr)
        gpyopt.run(dim=dim, itr=itr, init=init)
        RMSE_gene.run(init=init)
        print()
    print("--- finish ---", file=sys.stderr, end="\n\n")
