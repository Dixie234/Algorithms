from collections import deque


class MinStack:

    def __init__(self):
        self.min_vals = [float('inf')]
        self.stack = []
        
    def push(self, val: int) -> None:
        if val < self.min_vals[-1]:
            self.min_vals.append(val)
        else:
            self.min_vals.append(self.min_vals[-1])
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_vals.pop()
        
    def top(self) -> int:
        return self.stack[-1]    

    def getMin(self) -> int:
        return self.min_vals[-1]
    
stack = MinStack()
stack.push(2)
stack.push(0)
stack.push(3)
stack.push(0)
print(stack.getMin())
stack.pop()
print(stack.getMin())
stack.pop()
print(stack.getMin())
stack.pop()
print(stack.getMin())

