from typing import List

#Use of monotonic stack to descending temperatures until a higher temp is found
#Then works through all elements which have a temp lower than the one found by looking at the difference in the indices
#Time complexity O(n) - In worst case of an ascending list, stack is poped n times and we traverse every element, therefore O(2n) simplifies to O(n)
#Space complexity O(n) - In worst case of descending list, stack stores every value, and result is n elements long. O(2n) simplifies to O(n)
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    result = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev = stack.pop()
            result[prev] = i - prev
        stack.append(i)
    return result