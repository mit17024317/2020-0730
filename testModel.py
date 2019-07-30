
from model import modelInterface


def testFunc(x=[]):
    y = 0
    for t in x:
        y += t**2
    return y


class testModel(modelInterface):
    def __init__(self, sampleX=None, sampleY=None):
        pass

    def getPredictValue(self, x, a=2.5, b=50, c=97.5):
        print("ERROR!! not define this method")
        print("'testModel.getPredictValue()'")
        exit()

    def getPredict(self, x):
        return testFunc(x) + 5

