def isIsomorphic(s: str, t: str) -> bool:
    s_dict = create_dict(s)
    t_dict = create_dict(t)
    if len(s_dict) != len(t_dict):
        return False
    for (s_val, t_val) in zip(s_dict.values(), t_dict.values()):
        if s_val != t_val:
            return False
    return True

def create_dict(s: str) -> dict[int, int]: 
    result = {}
    for i, char in enumerate(s):
        if char in result:
            result[char].append(i)
        else:
            result[char] = [i]
    return result

def isIsomorphic_fast(s: str, t: str) -> bool:
    indexS = [0] * 200 
    indexT = [0] * 200 
    
    length = len(s) 
    
    if length != len(t): 
        return False
    
    for i in range(length): 
        ord_s = ord(s[i])
        ord_t = ord(t[i])
        if indexS[ord_s] != indexT[ord_t]: 
            return False 
        
        indexS[ord(s[i])] = i + 1 
        indexT[ord(t[i])] = i + 1
    
    return True 

s = "egh" # ("dfgh" * 1000)
t = "add" # ("dfgh" * 1000)
result = isIsomorphic(s, t)
print(result)