from typing import List

def candy(ratings: List[int]) -> int:
    length = len(ratings)
    left = [0]
    for i in range(length - 1):
        if ratings[i + 1] > ratings[i]:
            left.append(left[i] + 1)
        else:
            left.append(0)                   

    right = [0]
    for i in range(length - 1):
        if ratings[length - 1 - i] < ratings[length - 2 - i]:
            right.append(right[i] + 1) 
        else:
            right.append(0)

    result = 0
    for a_i, b_i in zip(left, right[::-1]):
        if a_i > 0 and b_i > 0:
            result += max(a_i, b_i) + 1
        else:
            result += a_i + b_i + 1
    
    return result

list = [1,2,3,4,5,6,5,3,2,4,56,6]
candy(list)

def candy_fast(ratings: List[int]) -> int:
    # we know all get one candy
    candies = [1] * len(ratings)


    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    #print(candies)
    
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    #print(candies)
    return sum(candies)
        
