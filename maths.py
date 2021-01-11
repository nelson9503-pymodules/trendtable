
def slope(xlist, ylist):
    x = len(xlist)
    s1 = s2 = s3 = s4 = 0
    for i in range(0, x):
        s1 += (xlist[i] * ylist[i])
        s2 += xlist[i]
        s3 += ylist[i]
        s4 += xlist[i]**2
    a = x * s1
    b = s2 * s3
    c = x * s4
    d = s2**2
    m = (a-b)/(c-d)
    return m

def scaleData(data: list) -> list:
    """
    This method outputs a same scaled x, y data.
    """
    k = len(data)
    xlist = list(range(k))
    max_i = max(data)
    min_i = min(data)
    if max_i > min_i:
        diff = max_i - min_i
        for i in range(len(data)):
            data[i] = ((data[i] - min_i) / diff) * (k-1)
    else:
        data = [k-1] * len(data)
    return xlist, data