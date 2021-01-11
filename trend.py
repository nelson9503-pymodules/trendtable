import math
from .maths import (
    slope,
    scaleData
)


def calTrendVal(data: list) -> float:
    """
    Calculate the sigle trend value for data.
    """
    xlist, data = scaleData(data)
    s = slope(xlist, data)
    v = math.atan(s) * 180 / math.pi
    return round(v, 4)


def calTrendSerious(data: list, interval: int) -> dict:
    """
    Calculate a serious of trend values for the data.
    """
    trend = {}
    for i in range(interval, len(data)+1, interval):
        data_slice = data[:i+1]
        x = calTrendVal(data_slice)
        trend[i] = x
    return trend
