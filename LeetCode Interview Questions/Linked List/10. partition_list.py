from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition_1(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    if not head:
        return None
    if not head.next:
        return head
    
    dummy = ListNode(None, head)
    lt_end = dummy
    gt_start = None
    gt_end = None
    curr = head
    while curr:
        if curr.val >= x:
            if not gt_start:
                gt_start = curr

            while curr and curr.val >= x:
                gt_end = curr
                curr = curr.next

            if not curr:
                break

            gt_end.next = curr.next
            lt_end.next = curr
            curr.next = gt_start
            lt_end = curr
            curr = gt_end
            curr = curr.next

        else:
            lt_end.next = curr
            lt_end = curr
            curr = curr.next
            if gt_start:
                lt_end.next = gt_start
            if gt_end:
                gt_end.next = curr

    return dummy.next

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    if not head:
        return None
    if not head.next:
        return head
    
    lt_dummy = ListNode(None, head)
    gt_dummy = ListNode(None, None)
    lt_group = lt_dummy
    gt_group = gt_dummy

    while head:
        if head.val >= x:
            gt_group.next = head
            gt_group = head
        else:
            lt_group.next = head
            lt_group = head

        head = head.next
        
    gt_group.next = None
    lt_group.next = gt_dummy.next

    return lt_dummy.next

#[1,4,3,0,2,5,2]
node7 = ListNode(2, None)
node6 = ListNode(5, node7)
node5 = ListNode(2, node6)
node4 = ListNode(0, node5)
node3 = ListNode(3, node4)
node2 = ListNode(4, node3)
node1 = ListNode(1, node2)
x = 3
result = partition(node1, x)
print(result)
#Expected: [1,0,2,2,4,3,5]
