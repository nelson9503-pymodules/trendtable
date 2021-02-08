import math
from .maths import (
    slope,
    scaleData
)


def cal_trend_val(data: list) -> float:
    """
    Calculate the sigle trend value for data.
    """
    xlist, data = scaleData(data)
    s = slope(xlist, data)
    v = math.atan(s) * 180 / math.pi
    return round(v, 4)


def cal_trend_serious(data: list, interval: int) -> dict:
    """
    Calculate a serious of trend values for the data.

    example:

        data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        interval: 2

        output:
            {
                2: [trend val],
                4: [trend val],
                6: [trend val],
                8: [trend val],
                10: [trend val]
            }
    """
    trend = {}
    for i in range(interval, len(data)+1, interval):
        data_slice = data[-i:]
        x = cal_trend_val(data_slice)
        trend[i] = x
    return trend
