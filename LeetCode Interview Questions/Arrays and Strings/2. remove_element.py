from typing import List


nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums: List[int], val: int) -> int:
    n = len(nums) - 1
    k = n

    while(n >= 0):
        if(nums[n] == val):
            val_k = nums[k]
            val_n = nums[n]
            nums[n] = val_k
            nums[k] = val_n
            k -= 1
        n -= 1

    return k + 1

k = removeElement(nums, val)

print(k)
print(nums)
