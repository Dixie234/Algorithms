import math


def rangeBitwiseAnd(left: int, right: int) -> int:
    log_left = math.floor(math.log2(left)) if left > 0 else 0
    log_right = math.floor(math.log2(right)) if right > 0 else 0
    if abs(log_left - log_right) > 0 or log_left == 0 and log_right == 0:
        return 0
    else:
        return 2 ** log_left
    
