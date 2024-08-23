from typing import List


def isHappy(n: int) -> bool:
    start = sum_square_number(n)
    answers_been = set()

    while start != 1:
        if start in answers_been:
            return False
        else:
            answers_been.add(start)
            next_val = sum_square_number(start)
            start = next_val
    return True

def sum_square_number(n: int) -> int:
    return sum([int(char) ** 2 for char in str(n)])

n = 456876487348
result = isHappy(n)
print(result)
    