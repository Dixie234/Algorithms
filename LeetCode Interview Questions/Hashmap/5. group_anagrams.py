from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    mapping:dict[str, list[str]] = { 
        ''.join(sorted(strs[0])): [strs[0]]
    }
    for word in strs[1:]:
        word_sorted = ''.join(sorted(word))
        if word_sorted in mapping:
            mapping[word_sorted].append(word)
        else:
            mapping[word_sorted] = [word]
    return list(mapping.values())

strs = ["eat","tea","tan","ate","nat","bat"]
result = groupAnagrams(strs)
print(result)
