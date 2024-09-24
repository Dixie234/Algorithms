def mySqrt(x: int) -> int:
    lower = 0
    upper = x
    mid = (lower + upper) // 2
    while lower <= upper:
        mid = (lower + upper) // 2
        val = (mid * mid)
        if val == x:
            return mid
        elif val > x:
            upper = mid - 1
        elif val < x:
            lower = mid + 1
    val = mid * mid
    if val == x:
        return mid
    if val > x:
        return mid - 1
    if val < x:
        return mid


result = mySqrt(2147483647)
print(result)