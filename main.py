from logging import DEBUG, basicConfig, getLogger

import cson

from Functions.FunctionInterface import FunctionInterface
from Functions.FunctionSelector import selectFunction
from Optimizer.SurrogateOptimizer import SurrogateOptimizer

logger = getLogger(__name__)


if __name__ == "__main__":
    basicConfig(level=DEBUG)
    logger.debug("-- start optimization --")

    # input parameters
    with open("Parameters/20200212/00.cson", "r") as f:
        parameter = cson.load(f)

        # each parameters
        obj = parameter["obj"]
        dim: int = parameter["dim"]
        name: str = parameter["problem"]
        method: str = parameter["method"]

        p: FunctionInterface = selectFunction(name)

        opt: SurrogateOptimizer = SurrogateOptimizer(method)
        ans = opt.optimize(p, obj, dim)
