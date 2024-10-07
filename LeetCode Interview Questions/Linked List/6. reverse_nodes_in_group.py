from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 (-> None), 3
def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if k == 1:
        return head
    
    dummy = ListNode(None, head)
    curr = dummy
    end = None
    while curr.next:
        curr = curr.next
        long_enough, end_next = list_long_enough(curr, k)
        if long_enough:
            if end:              
                new_start, new_end = reverseList(curr, k)
                end.next = new_start
                end = new_end
                curr = new_end
                curr.next = end_next
            else:
                new_start, new_end = reverseList(head, k)
                head = new_start
                end = new_end
                curr = new_end
                curr.next = end_next
        else:
            end.next = curr
            break
    return head

# 1 -> 2 -> 3 (-> None), 3
def list_long_enough(head: Optional[ListNode], k: int) -> tuple[bool, Optional[ListNode]]:
    while head and k > 0:
        head = head.next
        k -= 1
    return k <= 0, head
    
# 1 -> 2 -> 3 (-> None), 3
# 1 <- 2 <- 3
# (1 -> 2 -> 3) -> 4 -> 5 -> 6 (-> None), 3
def reverseList(head: Optional[ListNode], k:int) -> Optional[ListNode]:
    node = None
    curr = head
    while curr and k > 0:
        temp = curr.next
        curr.next = node
        node = curr
        curr = temp
        k -= 1
 
    return node, head
