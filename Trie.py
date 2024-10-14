from typing import List, Optional


class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word:str) -> Optional[TrieNode]:
        curr = self.root

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return None
            
        return curr
    
    def insert(self, word:str) -> None:
        curr = self.root

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                newNode = TrieNode()
                curr.children[char] = newNode
                curr = newNode

        curr.children["*"] = None

    def collect_all_words(self, node:TrieNode=None, word:str="", words:List[str]=[]) -> List[str]:
        curr = node or self.root

        for key, childNode in curr.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collect_all_words(childNode, word + key, words)
        
        return words
    
    def auto_complete(self, prefix:str) -> Optional[List[str]]:
        curr = self.search(prefix)
        if not curr:
            return None
        else:
            return self.collect_all_words(curr)