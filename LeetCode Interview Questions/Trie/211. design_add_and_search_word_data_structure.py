class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode()
                node.children[char] = new_node
                node = node.children[char]
        node.end_node = True

    #Uses dfs to recursively look for the correct path
    def search(self, word: str) -> bool:
        def dfs(node:TrieNode, i):
            if i == len(word): 
                return node.end_node
               
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i + 1): 
                        return True
                    
            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)
            
            return False

        return dfs(self.root, 0)