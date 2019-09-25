
import sys
import gpyopt
import RMSE_gene

if __name__ == "__main__":

    # parameters
    title = "test"
    dim = 2
    itr = 2
    init = 5
    num = 2

    # run
    print(title)
    for i in range(1, num+1):
        print("-- {}th run-- ".format(i), file=sys.stderr)
        gpyopt.run(dim=dim, itr=itr, init=init)
        RMSE_gene.run(init=init)
        print()
