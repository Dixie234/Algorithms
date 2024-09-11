from collections import deque
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return None
    if not head.next:
        return head
    
    queue = deque()
    curr = head
    while curr:
        queue.append(curr.val)
        curr = curr.next

    queue.rotate(k)

    dummyHead = ListNode()
    curr = dummyHead
    for val in queue:
        curr.next = ListNode(val)
        curr = curr.next

    return dummyHead.next
    
node5 = ListNode(5, None)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

k = 2
result = rotateRight(node1, k)
print
