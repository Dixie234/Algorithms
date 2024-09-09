from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next:ListNode = None

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:
        return None
    elif not list2:
        return list1
    elif not list1:
        return list2
    
    tail = None
    start = None
    while list1 and list2:
        if list1.val <= list2.val:
            node = list1
            list1 = list1.next if list1 else None
        else:
            node = list2
            list2 = list2.next if list2 else None

        if not tail:
            tail = node
            start = tail
        else:
            tail.next = node
            tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return start