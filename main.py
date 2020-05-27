import sys
from logging import DEBUG

import colorlog
import cson

from Functions.FunctionInterface import FunctionInterface
from Functions.FunctionSelector import selectFunction
from Optimizer.SurrogateOptimizer import SurrogateOptimizer

logger = colorlog.getLogger(__name__)

args = sys.argv

if __name__ == "__main__":
    formatter = (
        "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
    )
    colorlog.basicConfig(level=DEBUG, format=formatter)

    # parameter check
    if len(args) < 2:
        logger.critical(
            "Need Input Parameters! You should add filename to command line."
        )
        sys.exit(1)

    with open(args[1], "r") as f:
        # input parameters
        parameter = cson.load(f)

        # each parameters
        trial: int = parameter["trial"]
        ini: int = parameter["ini"]
        gen: int = parameter["gen"]
        obj: int = parameter["obj"]
        dim: int = parameter["dim"]
        name: str = parameter["problem"]
        method: str = parameter["method"]
        methodParam = parameter[method]

        p: FunctionInterface = selectFunction(name)

        # n trial
        for t in range(trial):
            # optimize start
            logger.info(f"-- start {t} trial optimization --")
            SurrogateOptimizer().optimize(
                prob=p,
                method=method,
                obj=obj,
                dim=dim,
                methodParam=methodParam,
                initialNum=ini,
                generations=gen,
            )
