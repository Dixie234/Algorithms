from typing import List, Optional

#A Trie is a special form of N-ary Tree which is used to store strings. Each Trie node represents a string (prefix).
#Paths to child nodes represent different characters, the strings in the child node represent the addition of that
#character as well as the origin string. e.g. "a" --> "ab"
#The root node is represented as an empty string. 
#All decendants of a node share the same prefix string, which is why it's sometimes called a "Prefix Tree".
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False

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

        curr.end_node = True

    def delete(self, word:str) -> None:
        curr = self.root
        def dfs(curr:TrieNode, index=0):
            if not curr.children:
                return False
            
            result = dfs(curr.children[word[index]], index + 1)
            if not result:
                del curr.children[word[index]]
            if not curr.children:
                return False

            return True
        
        dfs(curr)
        

    def collect_all_words(self, node:TrieNode=None, word:str="", words:List[str]=[]) -> List[str]:
        curr = node or self.root

        for key, childNode in curr.children.items():
            if curr.end_node:
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
        

trie = Trie()
trie.insert("rat")
trie.insert("car")
trie.insert("ran")
trie.insert("the")
trie.delete("rat")
print(trie)

#Another way of implementing the Trie can be to use a ordinal character array for each node instead of a dictionary.
#This requires additional methods to be part of the Node class.

class TrieNode:
    def __init__(self):
        self.children = [None] * 26

    def _contains(self, character:str) -> bool:
        return self.children[ord(character) - ord("a")] is not None

    def _put(self, character:str, node:"TrieNode") -> None:
        self.children[ord(character) - ord("a")] = node
    
    def _next(self, character:str) -> "TrieNode":
        return self.children[ord(character) - ord("a")]
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str) -> None:
        curr = self.root

        for char in word:
            if not curr._contains(char):
                curr._put(char, TrieNode())
            curr = curr._next(char)

    def search(self, word:str) -> bool:
        curr = self.root

        for char in word:
            if not curr._contains(char):
                return False
            curr = curr._next(char)
        return True
