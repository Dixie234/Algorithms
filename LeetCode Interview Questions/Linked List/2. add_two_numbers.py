from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next:ListNode = None
        
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    tail = None
    start = None
    while l1 or l2 or carry != 0:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        val = total % 10
        carry = total // 10

        node = ListNode(val)

        if not tail:
            tail = node
            start = tail
        else:
            tail.next = node
            tail = tail.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return start

# node1 = ListNode(2)
# node2 = ListNode(4)
# node3 = ListNode(3)
# node1.next = node2
# node2.next = node3

# node1_2 = ListNode(5)
# node2_2 = ListNode(6)
# node3_2 = ListNode(4)
# node1_2.next = node2_2
# node2_2.next = node3_2
node1 = ListNode(0)
node1_2 = ListNode(0)
result = addTwoNumbers(node1, node1_2)
print(result)

            