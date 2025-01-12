
#Very similar to problem 2116. check_parenthese_can_be_valid.
#Loop through all characters inside the string. Add any opening parenthese to the stack, and any astricks to the astrick stack.
#If encountering a closed paraenthese, prioritise popping from the stack, otherwise pop from the astricks as a replacement.
#Once loop is complete any outstanding open parenthese will still remain in the stack.
#These have to be matched with indexes greater than themselves as the open must always be before the close.
#Therefore, match the remaining open brackets to the astricks remaining, if there are any left or the index is too large
#then return False, otherwise all paranthese have been matched and return True.
#Time Complexity O(n) - Iterate through the characters of the string, and all remaining inside the stack which can't be greater than n.
#Space Complexity O(n) - 2 Stacks each which in worst case would hold every character from s.
def checkValidString(s: str) -> bool:
    length = len(s)
    
    stack = []
    astricks = []
    for i in range(length):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == "*":
            astricks.append(i)
        else:
            if stack:
                stack.pop()
            elif astricks:
                astricks.pop()
            else:
                return False
    while stack and astricks and stack[-1] < astricks[-1]:
        stack.pop()
        astricks.pop()

    return not stack

s = "(*)"
result = checkValidString(s)
