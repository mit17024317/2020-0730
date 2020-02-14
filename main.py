import sys
from logging import DEBUG, basicConfig, getLogger

import cson

from Functions.FunctionInterface import FunctionInterface
from Functions.FunctionSelector import selectFunction
from Optimizer.SurrogateOptimizer import SurrogateOptimizer

logger = getLogger(__name__)

args = sys.argv

if __name__ == "__main__":
    basicConfig(level=DEBUG)

    # parameter check
    if len(args) < 2:
        logger.critical(
            "Need Input Parameters! You should add filename to command line."
        )
        sys.exit(1)

    with open(args[1], "r") as f:
        logger.info("-- start Input Parameters -- ")
        # input parameters
        parameter = cson.load(f)

        # each parameters
        ini: int = parameter["ini"]
        gen: int = parameter["gen"]
        obj = parameter["obj"]
        dim: int = parameter["dim"]
        name: str = parameter["problem"]
        method: str = parameter["method"]

        p: FunctionInterface = selectFunction(name)

        # optimize start
        logger.info("-- start optimization --")
        opt: SurrogateOptimizer = SurrogateOptimizer(method)
        ans = opt.optimize(p, obj, dim, ini, gen)
