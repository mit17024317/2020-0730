from logging import DEBUG, basicConfig, getLogger

import cson

from Functions.FunctionInterface import FunctionInterface
from Functions.FunctionSelector import selectFunction

logger = getLogger(__name__)


if __name__ == "__main__":
    basicConfig(level=DEBUG)
    logger.debug("-- start optimization --")

    # input parameters
    with open("Parameters/sample.cson", "r") as f:
        parameter = cson.load(f)

        # each parameters
        obj = parameter["obj"]
        dim: int = parameter["dim"]
        name: str = parameter["problem"]

        p: FunctionInterface = selectFunction(name)
