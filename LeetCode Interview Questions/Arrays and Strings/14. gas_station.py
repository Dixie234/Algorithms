from collections import deque
from itertools import accumulate
from typing import List

#finds the minimum of the cumulative sum and takes the index after that
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    min_index = 0
    cum_sum = 0
    min_cum_sum = 0
    total_gas = 0
    total_cost = 0
    for i in range(len(gas)):
        diff = cum_sum + (gas[i] - cost[i])
        if diff < 0:            
            if diff < min_cum_sum:
                min_index = i + 1
                min_cum_sum = diff
        cum_sum = diff
        total_gas += gas[i] 
        total_cost += cost[i]
    if total_gas < total_cost:
        return -1 
    return min_index

def canCompleteCircuit_simple(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    total = 0
    res = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            total = 0
            res = i + 1
    
    return res

def canCompleteCircuit_slow(gas: List[int], cost: List[int]) -> int:
    if sum(cost) > sum(gas):
        return -1
    else:
        cum_sum = list(accumulate([(a_i - b_i, (a_i - b_i) > 0) for a_i, b_i in zip(gas, cost)]))
        if all([i > 0 for i in cum_sum[1]]):
            return 0
        index = 0 if min(range(len(cum_sum[0])), key=cum_sum[0].__getitem__) == len(gas) - 1 else min(range(len(cum_sum)), key=cum_sum.__getitem__) + 1
    return index

#fill up with gas[i]
#pay for travel to gas[i+1] with cost[i]
#fill up with gas[i+1]

#0 + 4 --im now at i
#4 - 1 --i've made my travel because 4 - 1 > 0
# list1 = [1,2,3,4,5]
# list2 = [3,4,5,1,2]

# list1 = [2,3,4]
# list2 = [3,4,3]

# gas = [2,0,0,0,0,0,0,0,0]
# cost = [0,1,0,0,0,0,0,0,0]
list1 = [6,1,4,3,5]
list2 = [3,8,2,4,2]

result = canCompleteCircuit(list1, list2)
print(result)





