from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:        
    word_mapping = { word: word for i, word in enumerate(wordDict) }
    def check_words(s):
        if s in word_mapping:
            return True
        
        build_str = ""
        possible_words = []
        for char in s:
            build_str += char
            if build_str in word_mapping:
                possible_words.append(build_str)
        
        if not possible_words:
            return False
        
        for word in possible_words:
            result = check_words(s[len(word):])
            if result:
                return True
            
        return False
    result = check_words(s)

    return result

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
result = wordBreak(s, wordDict)
print(result)
