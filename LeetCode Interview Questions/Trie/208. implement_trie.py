class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:

    def __init__(self): 
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode()
                node.children[char] = new_node
                node = node.children[char]
        node.children["*"] = None
        

    def search(self, word: str) -> bool:
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        if "*" in node.children:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)