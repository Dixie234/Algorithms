from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False

class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()      

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self._insert(word)
 
    def _insert(self, word:str) -> None:
        curr = self.root

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                new_node = TrieNode()
                curr.children[char] = new_node
                curr = new_node
        curr.end_node = True   

    def search(self, searchWord: str) -> bool:
        curr = self.root

        for char in searchWord:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return curr.end_node