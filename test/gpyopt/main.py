
import sys
import gpyopt
import RMSE_gene

if __name__ == "__main__":

    # parameters
    dim = 50
    itr = 30
    init = 5
    num = 5

    # run
    for i in range(1, num+1):
        print("-- {}th run-- ".format(i), file=sys.stderr)
        gpyopt.run(dim=dim, itr=itr, init=init)
        RMSE_gene.run(init=init)
        print()
