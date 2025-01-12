
#Very similar to problem 678. valid_parentese_string.
#Loop through all characters inside the string. Add any opening parenthese to the stack, and any unlocked to the unlocked stack.
#If encountering a closed paraenthese, prioritise popping from the stack, otherwise pop from the unlocked as a replacement.
#Once loop is complete any outstanding open parenthese will still remain in the stack.
#These have to be matched with indexes greater than themselves as the open must always be before the close.
#Therefore, match the remaining open brackets to the unlocked remaining, if there are any left or the index is too large
#then return False, otherwise all paranthese have been matched and return True.
#Time Complexity O(n) - Iterate through the characters of the string, and all remaining inside the stack which can't be greater than n.
#Space Complexity O(n) - 2 Stacks each which in worst case would hold every character from s.
def canBeValid(s: str, locked: str) -> bool:
    length = len(s)
    if len(s) % 2 == 1:
        return False
    
    stack = []
    unlocked = []
    for i in range(length):
        if locked[i] == "0":
            unlocked.append(i)
        elif s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            if stack:
                stack.pop()
            elif unlocked:
                unlocked.pop()
            else:
                return False
            
    while stack and unlocked and stack[-1] < unlocked[-1]:
        stack.pop()
        unlocked.pop()
    
    return not stack

s = "()))"
locked = "0010"
result = canBeValid(s, locked)