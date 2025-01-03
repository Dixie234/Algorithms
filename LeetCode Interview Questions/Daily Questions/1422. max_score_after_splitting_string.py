from collections import Counter

def maxScore(s: str) -> int:
    s_right_counter = Counter(s)
    s_left_counter = {
        "0": 0,
        "1": 0
    }
    score = 0
    for i in range(len(s) - 1):
        s_left_counter[s[i]] += 1
        s_right_counter[s[i]] -= 1
        score = max(score, (s_left_counter["0"] + s_right_counter["1"]))
    return score
