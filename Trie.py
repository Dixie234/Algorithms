from typing import List, Optional

#A Trie is a special form of N-ary Tree which is used to store strings. Each Trie node represents a string (prefix).
#Paths to child nodes represent different characters, the strings in the child node represent the addition of that
#character as well as the origin string. e.g. "a" --> "ab"
#The root node is represented as an empty string. 
#All decendants of a node share the same prefix string, which is why it's sometimes called a "Prefix Tree".
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