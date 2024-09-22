import math


def addBinary(a: str, b: str) -> str:
    num_a = 0
    num_b = 0

    for char in a:
        num_a = num_a * 2 + int(char)
    for char in b:
        num_b = num_b * 2 + int(char)

    result_num = num_a + num_b
    if result_num == 0:
        return "0"
    
    length = math.floor(math.log2(result_num))

    result = ""
    for i in range(length, -1, -1):
        num = 2 ** i
        if (result_num - num) < 0:
            result += "0"
        else:
            result += "1"
            result_num -= num

    return result

def addBinary_simple(a: str, b: str) -> str:
    res = int(a, 2) + int(b, 2)
    return format(res, 'b')