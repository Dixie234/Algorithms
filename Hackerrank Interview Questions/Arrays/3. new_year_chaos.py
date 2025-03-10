from typing import List


def minimumBribes(q:List[int]):
    length = len(q)
    correct_queue = [i for i in range(1, length + 1)]
    swaps = 0
    i = 0
    while i < length - 1:
        if q[i] != correct_queue[i]:
            temp_i = i
            moves = 0
            while q[temp_i] != correct_queue[temp_i]:
                if moves == 2:
                    print("Too chaotic")
                    return
                
                q[temp_i], q[temp_i + 1] = q[temp_i + 1], q[temp_i]
                temp_i += 1
                moves += 1
                swaps += 1
        else:
            i += 1
    print(swaps)

q = [1,2,5,3,7,8,6,4]
minimumBribes(q)




