from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:ListNode = next

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head:
        return None
    if not head.next:
        return head
    if left == right:
        return head 
    
    counter = 1
    curr = head
    sub_head:ListNode = None
    sub_tail:ListNode = None
    reattach_left_next = None
    reattach_right_node = None
    while counter <= right:
        if counter == (left - 1):
            reattach_left_next = curr
        elif counter == left:
            sub_head = curr
        elif counter == right:
            sub_tail = curr
            if curr.next:
                reattach_right_node = curr.next
        curr = curr.next
        counter += 1
    
    sub_tail.next = None
    new_sub_head, new_sub_tail = reverseList(sub_head)

    if left == 1:
        head = new_sub_head
    if reattach_left_next:
        reattach_left_next.next = new_sub_head
    if reattach_right_node:
        new_sub_tail.next = reattach_right_node

    return head


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    if not head.next:
        return head

    prev_next = None
    prev = head
    curr = head.next
    while curr.next:
        prev.next = prev_next
        prev_next = prev
        prev = curr
        curr = curr.next
    
    prev.next = prev_next
    curr.next = prev
    return curr, head
