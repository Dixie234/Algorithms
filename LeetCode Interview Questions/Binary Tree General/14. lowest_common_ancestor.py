from collections import deque


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def lowestCommonAncestor_too_slow(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    left_p = try_find_node(root.left, p)
    left_q = try_find_node(root.left, q)

    if left_p and left_q:
        return lowestCommonAncestor_too_slow(root.left, p, q)
    elif try_find_node(root.right, p) and try_find_node(root.right, q):
        return lowestCommonAncestor_too_slow(root.right, p, q)
    else:
        return root

def try_find_node(root: 'TreeNode', node: 'TreeNode') -> bool:
    if not root:
        return
    
    if root.val == node.val:
        return True

    if try_find_node(root.left, node):
        return True
    else:
        return try_find_node(root.right, node)

#Using Arrays  
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    p_path = []
    q_path = []
    find_p = findPath(root, p_path, p.val)
    find_q = findPath(root, q_path, q.val)

    i = 0
    while(i < len(p_path) and i < len(q_path)):
        if p_path[i] != q_path[i]:
            break
        i += 1
    return p_path[i-1] 


def findPath(root, path, val):
    if not root:
        return False

    path.append(root.val)

    if root.val == val:
        return True

    if ((root.left != None and findPath(root.left, path, val)) or
            (root.right != None and findPath(root.right, path, val))):
        return True

    path.pop()
    return False

#Using traversal
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root

    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p, q)

    if l and r:
        return root
    return l or r

node9 = TreeNode(0)
node10 = TreeNode(8)
node1 = TreeNode(1, node9, node10)

node4 = TreeNode(6)

node7 = TreeNode(7)
node8 = TreeNode(4)

node5 = TreeNode(2, node7, node8)

node2 = TreeNode(5, node4, node5)
node3 = TreeNode(3, node2, node1)

result = lowestCommonAncestor(node3, node7, node8)
print(result)
