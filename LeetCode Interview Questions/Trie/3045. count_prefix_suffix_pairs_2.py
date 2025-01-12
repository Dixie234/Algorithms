from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str) -> None:
        curr = self.root 

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                new_node = TrieNode()
                curr.children[char] = new_node
                curr = new_node
    
    def search(self, word:str) -> bool:
        curr = self.root

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True


def countPrefixSuffixPairs(words: List[str]) -> int:
    result = 0

    for i in range(len(words)):
        prefixTrie = Trie()
        suffixTrie = Trie()

        prefixTrie.insert(words[i])
        suffixTrie.insert(words[i][::-1])

        for j in range(i):
            if len(words[j]) > len(words[i]):
                continue

            word = words[j]
            re_word = words[j][::-1]
            if prefixTrie.search(word) and suffixTrie.search(re_word):
                result += 1
    return result

words = ["pa","papa","ma","mama"]
result = countPrefixSuffixPairs(words)

#Use defaultdict to represent the Trie
def countPrefixSuffixPairs(words: List[str]) -> int:
    root = (T := lambda: defaultdict(T))()
    result = 0

    for word in words:
        curr = root
        for char in zip(word, reversed(word)):
            result += (curr := curr[char]).get(0, 0)
        curr[0] = curr.get(0, 0) + 1
    return result

def countPrefixSuffixPairs(words: List[str]) -> int:
    def create_node():
        return defaultdict(create_node)

    root = create_node()
    result = 0

    for word in words:
        curr = root
        for char_pair in zip(word, reversed(word)):
            char = char_pair
            curr = curr[char]       # Move to the next node
            result += curr.get(0, 0)
        curr[0] = curr.get(0, 0) + 1

    return result

words = ["pa","papa","ma","mama"]
result = countPrefixSuffixPairs(words)
        

