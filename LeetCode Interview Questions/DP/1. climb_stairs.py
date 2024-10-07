def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    
    prev_prev = 1
    prev = 1
    total = 0
    for i in range(n + 1):
        if i > 1:
            total = prev_prev + prev
            prev_prev = prev
            prev = total
    return total