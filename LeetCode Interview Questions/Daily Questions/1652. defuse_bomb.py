from typing import List

# 0 1 2 3 
#[1,2,3,4]
#k = 3
#1,2,3
#2,3,4
#3,4,5
#4,5,6

# if i >= length: i -= length

# 0 1 2 3 
#[1,2,3,4]
#k = -3
#-1,-2,-3
#0,-1,-2
#1,0,-1
#2,1,0

# if (i + j) < 0: i += length

def decrypt(code: List[int], k: int) -> List[int]:
    length = len(code)
    if k == 0:
        return [0] * length
    elif k > 0:
        new_list = []
        for i in range(length):
            total = 0
            for j in range(1, k + 1):
                if (i + j) >= length:
                    index = (i + j) - length
                else:
                    index = i + j
                total += code[index]
            new_list.append(total)
        return new_list
    else:
        new_list = []
        for i in range(length):
            total = 0
            for j in range(-1, k - 1, -1):
                if (i + j) < 0:
                    index = (i + j) + length
                else:
                    index = i + j
                total += code[index]
            new_list.append(total)
        return new_list
      
            
    
    
    