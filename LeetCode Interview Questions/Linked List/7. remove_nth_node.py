from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# remove from the middle
#[1, 2, 3, 4]
# n = 2
# remove 3 at index 2
# counter = 4
# counter - n > 0 therefore there is a node before the one removed
# node before = 2
# 2.next now needs to = 4

# remove from the beginning
#[1, 2, 3, 4]
# n = 4
# remove 1 at index 0
# counter = 4
# counter - n == 0 therefore its the beginning of the list 
# head becomes head.next 

# remove from the end
#[1, 2, 3, 4]
# n = 1
# remove 4 at index 3
# counter = 4
# n == 1 therefore it is the end node, node before next needs to be None
# node before = 3
# 3.next = None

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head:
        return None
    if not head.next:
        return None
    
    counter = 1
    node_n_behind = None
    prev_node = None
    curr = head
    while curr:
        if counter >= n:
            if node_n_behind:
                prev_node = node_n_behind
                node_n_behind = node_n_behind.next
            else:
                node_n_behind = head
        curr = curr.next 
        counter += 1

    #remove from the end of the list
    if n == 1:
        prev_node.next = None   
    #remove from the beginning of the list
    elif (counter - 1) == n:
        head = head.next
    #remove from the middle of the list
    else: 
        prev_node.next = node_n_behind.next
    
    return head


    


