from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:        
    word_mapping = set(wordDict)
    memo = {}
    def check_words(s):
        if s in memo:
            return memo[s]
        if s in word_mapping:
            return True
        
        build_str = ""
        for i, char in enumerate(s):
            build_str += char
            if build_str in word_mapping and check_words(s[i + 1:]):
                memo[s] = True
                return True
        memo[s] = False

        return False
    
    return check_words(s)   

def wordBreak_unintuative(s: str, wordDict: List[str]) -> bool:
    dp = [True] + [False] * len(s)

    for i in range(1, len(s) + 1):
        for w in wordDict:
            start = i - len(w)
            if start >= 0 and dp[start] and s[start:i] == w:
                dp[i] = True
                break
    return dp[-1]
    

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
result = wordBreak(s, wordDict)
print(result)
