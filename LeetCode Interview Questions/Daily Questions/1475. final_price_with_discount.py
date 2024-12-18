from typing import List

#Brute force approach using a nested loop which short circuits then a result is found
#Time complexity O(n^2) - in worst case of asecending sequence the entire array is scanned for every value
#Space complexity O(1) - all updates happen in place
def finalPrices(prices: List[int]) -> List[int]:
    for i in range(len(prices) - 1):
        for j in range(1 + i, len(prices)):
            if prices[i] >= prices[j]:
                prices[i] = prices[i] - prices[j]
                break
    return prices

#Use monotonic stack to keep track of acending values in the array
#Once you come across a value less than the last value in the stack, 
#you work through the stack applying discounts until you're unable to.
#Those which never find a discount are left in the stack and not changed.
#Time Complexity - O(n) - Worst case would be 2 * n operations where you pop for every iteration. This is simplified to O(n).
#Space Complexity - O(n) - In worst case of ascending array, stack will hold all values 
def finalPrices(prices: List[int]) -> List[int]:
    stack = []

    for i, val in enumerate(prices):
        while stack and prices[stack[-1]] >= val:
            prev_index = stack.pop()
            prices[prev_index] -= val
        stack.append(i)
    return prices

l = [1,2,3,4,5,1]
result = finalPrices(l)
print(result)



