#!/usr/bin/env python3
"""Result parser"""

__author__ = "R.Nakata"
__date__ = "2020/02/17"

import csv

import numpy as np


class Parser:
    def __read(self, filename) -> np.ndarray:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            return np.array([row for row in reader])

    def __toAverage(self, rawData, gen) -> np.ndarray:
        floatData: np.ndarray = np.frompyfunc(float, 1, 1)(rawData)
        aveData: np.ndarray = floatData[:gen]
        trial: int = int(len(floatData) / gen)
        for f in range(gen, trial * gen, gen):
            aveData += floatData[f : f + gen]
        aveData /= trial

        return aveData

    def parse(self, filename, gen) -> np.ndarray:
        rawData: np.ndarray = self.__read(filename)
        processedData: np.ndarray = self.__toAverage(rawData, gen)
        tData = processedData.T
        return tData
