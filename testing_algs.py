from collections import deque
from typing import List, Optional

### arrays ###

#return the maximum sub array from an array
def kadanes(arr:List[int]) -> int:
    result = - float("inf")
    curr_sum = - float("inf")
    for val in arr:
        curr_sum = max(curr_sum + val, val)
        result = max(curr_sum, result)
    return result

#return the index for a given search value in a sorted array
def binary_search(arr:List[int], val:int):
    low = 0
    high = len(arr) -1
    while low <= high:
        med = (low + high) // 2
        if arr[med] == val:
            return med
        elif arr[med] > val:
            high = med - 1
        else:
            low = med + 1
    return -1

### queues ###

#monotonic increasing queue
def monotonic_increasing(arr:List[int]):
    q = deque()
    for i in range(len(arr)):
        while q and q[-1] > arr[i]:
            q.pop()
        q.append(arr[i])
    return q

#monotonic decreasing queue
def monotonic_decreasing(arr:List[int]):
    q = deque()
    for i in range(len(arr)):
        while q and q[-1] < arr[i]:
            q.pop()
        q.append(arr[i])
    return q

### trees ###
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root:TreeNode) -> None:
    if not root:
        return None
    
    q = deque([root])
    while q:
        for i in range(len(q)):
            val = q.popleft()
            print(val)
            if val.left:
                q.append(val.left)
            if val.right:
                q.append(val.right)

def dfs_preorder(root:TreeNode) -> None:
    if not root:
        return
    
    print(root.val)
    dfs_preorder(root.left)
    dfs_preorder(root.right)

def dfs_inorder(root:TreeNode) -> None:
    if not root:
        return
    
    dfs_inorder(root.left)
    print(root.val)
    dfs_inorder(root.right)

def dfs_postorder(root:TreeNode) -> None:
    if not root:
        return
    
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.val)

### trie ###

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
                curr = curr.children
            else:
                new_node = TrieNode()
                curr.children[char] = new_node
                curr = new_node
        curr.end_node = True

    def delete(self, word:str) -> None:
        curr = self.root

        def dfs(node:TrieNode, index=0):
            if node not in curr.children:
                return False
            
            result = dfs(node.children[word[index]], index + 1)
            if not result:
                del curr.children[word[index]]
            else:
                return False
            
            return True
        
        dfs(curr)

### graphs ###
class GraphNode:
    def __init__(self, val=0):
        self.val = val
        self.adjacent_verticies:List["GraphNode"] = []

    def add_adjacent_vertex(self, vertex:"GraphNode"):
        if vertex not in self.adjacent_verticies:
            self.adjacent_verticies.append(vertex)


def bfs(root:GraphNode):
    q = deque([root])
    visited = {
        root.val: True
    }
    while q:
        for i in range(len(q)):
            val = q.popleft()
            for vertex in val.adjacent_verticies:
                if vertex.val not in visited:
                    visited[vertex.val] = True
                    q.append(vertex)

def dfs(root:GraphNode, visited={}):
    visited[root.val] = True
    
    print(root.val)

    for vertex in root.adjacent_verticies:
        if vertex.val not in visited:
            dfs(vertex, visited)

    



    
