<<<<<<< HEAD
def minimumBribes(q):
    too_chaotic = False
    for i, mem in enumerate(q):
        original_position = i + 1
        diff = mem - original_position
        if diff >= 3:
            too_chaotic = True
            break
    if too_chaotic:
        print("Too chaotic")
        return
    original = [i for i in range(1, len(q) + 1)]
    q_map = { k: i for i, k in enumerate(q) }    
    result = 0
    for i in range(len(q)):
        if original[i] != q[i]:
            ind = q_map[original[i]]
            q[i], q[ind] = q[ind], q[i]

            q_map[q[i]] = i
            q_map[q[ind]] = ind
            result += 1
    print(result) 

l = [2,1,5,3,4]
o = [1,2,3,4,5]

l = [1,2,5,3,7,8,6,4]
o = [1,2,3,4,5,6,7,8]
minimumBribes(l)
=======
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




>>>>>>> e841595648699c5d5034afe5a00efe81127aac8b
