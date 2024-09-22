from collections import deque


def plus(right,left):
    return int(left) + int(right)

def minus(right,left=None):
    if left:
        return int(left) - int(right)
    else:
        return - int(right)
    
op_mapping = {
    "+": plus,
    "-": minus
}

def calculate(s: str) -> int:
    calc_stack = []
    bracket_indexes = []
    for i, char in enumerate(s):
        if char == " ":
            continue

        if char == "(":
            bracket_indexes.append(i)
        elif char == ")":
            previous_bracket = bracket_indexes.pop()
            stack = s[previous_bracket + 1 : i]
            if len(bracket_indexes) == 0:
                calc_stack.append(calculate(stack))
        else:
            if len(bracket_indexes) == 0:
                calc_stack.append(char)
    result = evaluate(calc_stack)
    return int(result)

def evaluate(exp:list):
    s_stack = deque()
    num_str = ""
    for char in exp:
        if char == " ":
            continue
        
        if char in op_mapping:
            if num_str:
                s_stack.append(num_str)
                num_str = ""
            s_stack.append(char)
        else:
            num_str += str(char)
    if num_str:
        s_stack.append(num_str)

    calc_stack = []

    while len(s_stack) > 0:
        val = s_stack.popleft()
        if val in op_mapping:
            left = None
            if calc_stack:
                left = calc_stack.pop()
            right = s_stack.popleft()
            calc_result = op_mapping[val](right, left)
            calc_stack.append(calc_result)
        else:
            calc_stack.append(val)
    return calc_stack[0]


#"- 1 + 4 + 5 + 2 - 3 - 6 + 8 "
# "(1+(4+5+2)-3)+(6+8)"
# "0"
# 2147483647
s = "(1+(4+5+2)-3)+(6+11)"
result = calculate(s)
print(result)