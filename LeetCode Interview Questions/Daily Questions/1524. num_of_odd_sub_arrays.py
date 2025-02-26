from typing import List


def numOfSubarrays(arr: List[int]) -> int:
    odd_sums = 0
    for i in range(arr):
        if arr[i] % 2 == 1:
            odd_sums += 1
        cum_sum = 0
        for j in range(i + 1, arr):
            cum_sum += arr[j]
            curr_summ = arr[i] + cum_sum
            if curr_summ % 2 == 1:
                odd_sums += 1

    return odd_sums