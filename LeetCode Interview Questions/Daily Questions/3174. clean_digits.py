
#Create stack of chars which aren't numeric
#If you come across a number string, don't append it, and remove 1 from the stack
#Time complexity O(n) - Iterates through every char in the string, and then again to covert the stack into a string again
#Space complexity O(n) - In worst case creates a stack of every char in the string
def clearDigits(s: str) -> str:
    stack = []
    for char in s:
        if char.isnumeric():
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

