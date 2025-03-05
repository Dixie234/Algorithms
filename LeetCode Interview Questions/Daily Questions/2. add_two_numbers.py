from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Time complexity O(max(n, m)) - iterates through every node in both lists so is dependant on longest linked list
#Space Complexity O(max(n, m)) - result will be as long as the maximum linked list length, possible + 1 extra node which is constant and therefore ignored
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    curr = result
    carry = 0
    while l1 and l2:
        val = l1.val + l2.val + carry
        if val > 9:
            carry = 1
            val -= 10
        else:
            carry = 0
        node = ListNode(val)
        curr.next = node
        curr = curr.next
        l1 = l1.next
        l2 = l2.next
    if l1:
        while l1:
            val = l1.val + carry
            if val > 9:
                carry = 1
                val -= 10
            else:
                carry = 0
            node = ListNode(val)
            curr.next = node
            curr = curr.next
            l1 = l1.next
    if l2:
        while l2:
            val = l2.val + carry
            if val > 9:
                carry = 1
                val -= 10
            else:
                carry = 0
            node = ListNode(val)
            curr.next = node
            curr = curr.next
            l2 = l2.next
    if carry == 1:
        node = ListNode(carry)
        curr.next = node
    return result.next

#returns as int, not correct solution
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> int:
    multiplier = 0
    result = 0
    curr1 = l1
    curr2 = l2
    while curr1 and curr2:
        result += (curr1.val * (10**multiplier)) + (curr2.val * (10**multiplier))
        multiplier += 1
        curr1 = curr1.next
        curr2 = curr2.next
    if curr1:
        while curr1:
            result += (curr1.val * (10**multiplier))
            multiplier += 1
            curr1 = curr1.next
    if curr2:
        while curr2:
            result += (curr2.val * (10**multiplier))
            multiplier += 1
            curr2 = curr2.next
    return result
