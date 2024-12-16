from collections import deque
from typing import List

#use a dictionary to store the frequency of each value
#dictionaries retain order and therefore allow for log(n) maximum and minimum calculations
#Time complexity O(nlog(k)) - where k is the number of keys in the dictionary
#Space complexity O(k) ~ O(1) - since dictionary only holds at most 3 elements at any time
def continuousSubarrays(nums: List[int]) -> int:
    left = 0
    right = 0
    count = 0
    freq = {}
    while left < len(nums):
        freq[nums[left]] = freq.get(nums[left], 0) + 1

        while max(freq) - min(freq) > 2:
            freq[nums[right]] -= 1
            if freq[nums[right]] == 0:
                del freq[nums[right]]
            right += 1
        count += (left - right) + 1
        left += 1
        
    return count

#2nd approach using monotonic increasing and decreasing queues 
#allows of O(1) lookups for current maximum and minimum values
#Time complexity O(n) - even with the while loops since each element can only added or removed once from the queue
#Space complexity O(n) - although in worst case it's O(n) it's much more common to be less than that due to > 2 constraint
#Can achieve closer to O(1) space complexity by also removing elements equal to the incoming element from the queue,
#Therefore only allowing unique elements to be stored - which would be a maximum of 4 at any 1 time.
def continuousSubarrays(nums: List[int]) -> int:
    # Monotonic deque to track maximum and minimum elements
    max_q = deque()
    min_q = deque()
    left = 0
    count = 0

    for right, num in enumerate(nums):
        # Maintain decreasing monotonic deque for maximum values
        while max_q and nums[max_q[-1]] <= num:
            max_q.pop()
        max_q.append(right)

        # Maintain increasing monotonic deque for minimum values
        while min_q and nums[min_q[-1]] >= num:
            min_q.pop()
        min_q.append(right)

        # Shrink window if max-min difference exceeds 2
        while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] > 2:
            # Move left pointer past the element that breaks the condition
            if max_q[0] < min_q[0]:
                left = max_q[0] + 1
                max_q.popleft()
            else:
                left = min_q[0] + 1
                min_q.popleft()

        # Add count of all valid subarrays ending at current right pointer
        count += right - left + 1

    return count

nums = [3,4,3,3,2,1]
result = continuousSubarrays(nums)
print(result)



            