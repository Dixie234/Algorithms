import math

#1, 3, 9, 27, 81, 243
#Use espsilon when dealing with floats to account for rounding errors
def checkPowersOfThree(n: int) -> bool:
    used = set()
    epsilon = 1e-9
    while n != 0:
        start = math.floor(math.log(n, 3) + epsilon) 
        val = 3 ** start
        if val in used:
            return False
        n -= val
        used.add(val)
        if n < 0:
            return False
    return True

n = 6574365
result = checkPowersOfThree(n)
print(result)

    