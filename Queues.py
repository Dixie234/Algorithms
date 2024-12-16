from collections import deque

# Function to calculate Increasing
# Monotonic queue
def increasing_monotonic_queue(arr):
    n = len(arr)
    q = deque()
    for i in range(n):
        # If recently added element is
        # larger than current element
        while len(q) > 0 and q[-1] > arr[i]:
            q.pop()
        q.append(arr[i])
    return q
 
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
q = increasing_monotonic_queue(arr, n)
for i in q:
    print(i, end=' ')
 
# Function to calculate Decreasing
# Monotonic queue
def decreasing_monotonic_queue(arr):
    n = len(arr)
    q = deque()
    for i in range(n):
        # If recently added element is
        # smaller than current element
        while q and q[-1] < arr[i]:
            q.pop()
        q.append(arr[i])
    return q
 
# Driver Code
arr = [6, 5, 4, 3, 2, 1]
 
# Function call
q = decreasing_monotonic_queue(arr)
 
for i in q:
    print(i)