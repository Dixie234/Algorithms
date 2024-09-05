from math import ceil, floor
from typing import List

def plus(a,b):
    return a + b
def minus(a,b):
    return a - b
def divide(a,b):
    if (a < 0 and b >= 0) or (a >= 0 and b < 0):
        return ceil(a / b)
    else:
        return floor(a / b)
def multiply(a,b):
    return a * b

op_mapping = {
    "+": plus,
    "-": minus,
    "/": divide,
    "*": multiply
}

def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token in op_mapping:
            b = stack.pop()
            a = stack.pop()
            stack.append(op_mapping[token](a, b))
        else:
            stack.append(int(token))
    return stack[0]

#evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
result = evalRPN(["10", "11", "+"])
print(result)