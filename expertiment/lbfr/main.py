
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from models import LBFR


if __name__ == "__main__":
    print("hello ")
    v = LBFR.BasisVector(3)
    print(v.get([1.0,2.0,3.0]))
