from itertools import accumulate


def coloredCells(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result += (i - 1) * 4
    return result

def coloredCells(n: int) -> int:
    add = lambda prev, i: prev + (i - 1) * 4
    result = list(accumulate([i for i in range(2, n + 1)], func=add, initial=1))
    return result[0]