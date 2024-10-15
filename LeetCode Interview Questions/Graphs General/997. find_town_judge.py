from typing import List

#inefficent method using dictionary and sets
def findJudge(n: int, trust: List[List[int]]) -> int:
    adj = { i: set() for i in range(1, n + 1) }
    for edge in trust:
        adj[edge[0]].add(edge[1])

    adj_filtered = [k for k, v in adj.items() if len(v) == 0]
    if len(adj_filtered) == 0:
        return -1
    else:
        potentials = []
        for val in adj_filtered:
            for s in [v for k, v in adj.items() if k != val]:
                if val not in s:
                    return -1
            potentials.append(val)
        if len(potentials) == 1:
            return potentials[0]
        else:
            return -1

#optimal solution using incrementing counts    
def findJudge(n: int, trust: List[List[int]]) -> int:
    # you must traverse the entire list
    # for each person that trusts person P trusted_persons[P] += 1
    # for each person T that trusts anyone non_judges[].append(T)
    trust_going_out = [0]*n
    trust_coming_in = [0]*n
    for truster, trustee in trust:
        trust_coming_in[trustee] += 1
        trust_going_out[truster] += 1
    for i in range(1, n + 1):
        if trust_coming_in[i] == n - 1 and trust_going_out[i] == 0:
            return i
            
    return -1




