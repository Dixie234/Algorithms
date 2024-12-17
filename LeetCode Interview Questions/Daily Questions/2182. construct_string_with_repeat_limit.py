from collections import Counter
from heapq import heapify, heappop, heappush

#Greedy approach which tries to use the largest letter it can
#if it hits the limit then it looks through the array to find 
#the next character and applies it to the result string.
#Time complexity O(n * k) - where n is the number of characters and k is the unique characters in the string
#Space complexity O(k) - where k is the unique characters in the string (maximum of 26)
def repeatLimitedString(s: str, repeatLimit: int) -> str:
    s_map = [0] * 26
    start = ord("a")
    for c in s:
        index = ord(c) - start
        s_map[index] += 1

    result = ""
    for i in range(len(s_map) - 1, -1, -1):
        if s_map[i]:
            curr_repeat = 0
            while s_map[i] > 0:
                if curr_repeat == repeatLimit:
                    for k in range(i - 1, -1, -1):
                        if s_map[k]:
                            result += chr(k + start)
                            curr_repeat = 0
                            s_map[k] -= 1
                            break
                if curr_repeat == repeatLimit:
                    break
                result += chr(i + start)
                curr_repeat += 1
                s_map[i] -= 1

    return result

#Optimized approach which uses a max heap to track the best next letter to use
#This allow for O(log(n)) collection of next needed characters, rather than using a basic array
#Time Complexity O(n * log(k)) - where n is the number of characters and k is the unique characters in the string
#Space Complexity O(k) - where k is the unique characters in the string (maximum of 26)
def repeatLimitedString(s: str, repeatLimit: int) -> str:
    max_heap = [(-ord(c), count) for c, count in Counter(s).items()]
    heapify(max_heap)

    result = ""
    while max_heap:
        neg_ord, count = heappop(max_heap)
        char = chr(-neg_ord)
        uses = min(count, repeatLimit)
        result += char * uses

        if uses < count and max_heap:
            next_neg_ord, next_count = heappop(max_heap)
            char = chr(-next_neg_ord)
            result += char
            if next_count > 1:
                heappush(max_heap, (next_neg_ord, next_count - 1))
            heappush(max_heap, (neg_ord, count - uses))
    return result

s = "acacczazczczacazz"
repeatLimit = 3

#Calculate max lexiological string without constaint
def lex_max(s:str) -> str:
    s_map = [0] * 26
    start = ord("a")
    for c in s:
        index = ord(c) - start
        s_map[index] += 1

    result = ""
    for i in range(len(s_map) - 1, -1, -1):
        if s_map[i]:
            result += chr(i + start) * s_map[i]
    return result

result = repeatLimitedString(s, 3)
print(result)