from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#delete all nodes which had a duplicated value
# [1,2,3,3,4,5] -> [1,2,4,5]
# [1,1,2,3] -> [2,3]
# [1,2,3,3] -> [1,2]

# [none,1,2,3,3,4,5]
# curr.next.val = 2 != curr_val = 1 
# therefore set prev = curr which is 1 
# set curr to next which is 2

# none, 1 [2,3,3,4,5]
# curr.next.val = 3 != curr_val = 2
# therefore set prev = curr which is 2
# set curr to next which is 3

# none, 1, 2 [3,3,4,5]
# curr.next.val = 3 == curr_val = 3
# therefore prev.next (which is 3) is set to curr.next.next which is 4
# set curr to next which is 4

# none,1,2,3,3 [4,5]
# curr.next.val = 5 != curr_val = 4
# therefore set prev = curr which is 4
# set curr to next which is 5

# none,1,2,3,3,4 [5]
# curr.next == None
# therefore set curr to next which is None
# end of loop 

################################

# [none,1,2,3,4,5,5]
# curr.next.val = 2 != curr_val = 1 
# therefore set prev = curr which is 1 
# set curr to next which is 2

# none, 1 [2,3,4,5,5]
# curr.next.val = 3 != curr_val = 2
# therefore set prev = curr which is 2
# set curr to next which is 3

# none, 1 [2,3,4,5,5]
# curr.next.val = 4 != curr_val = 3
# therefore set prev = curr which is 3
# set curr to next which is 4

# none,1,2,3 [4,5,5]
# curr.next.val = 5 != curr_val = 4
# therefore set prev = curr which is 4
# set curr to next which is 5

# none,1,2,3,4 [5,5]
# curr.next.val = 5 == curr_val = 5
# therefore prev.next (which is 4) is set to curr.next.next which is None
# set curr to next.next which is None

# none,1,2,3,3,5 [5]
# curr.next is None therefore loop
# dummy.next = head

################################

# none [1,1,1,2,3,4,5]
# curr.next.val = 1 == curr_val = 1
# therefore prev.next (which is 1) is set to curr.next.next which is 1
# set curr to curr.next.next which is 1

# none,1,1 [1,2,3,4,5]
# curr.next.val = 2 != curr_val = 1
# therefore set prev = curr which is 1
# set curr to next which is 3

# none,1,1 [2,3,4,5]
# curr.next.val = 4 != curr_val = 3
# therefore set prev = curr which is 3
# set curr to next which is 4

# none,1,1,2 [3,4,5]
# curr.next.val = 5 != curr_val = 4
# therefore set prev = curr which is 4
# set curr to next which is 5

# none,1,1,2,3 [4,5]
# curr.next.val = 5 == curr_val = 5
# therefore prev.next (which is 4) is set to curr.next.next which is None
# set curr to next.next which is None

# none,1,1,2,3,4 [5]
# curr.next is None therefore loop
# dummy.next = head

################################

# none [1,2,2,3,3,5]
# curr.next.val = 2 != curr_val = 1
# therefore prev = curr (1) curr = curr.next (2)

# none,1 [2,2,3,3,5]
# curr.next.val = 2 == curr_val = 2
# therefore set prev.next (2) = curr.next (2)
# set curr = curr.next.next which is 3

# none,1,2,2 [3,3,5]
# curr.next.val = 3 == curr_val = 3
# therefore set prev = curr which is 3
# set curr to next which is 4

# none,1,2,2 [3,3,5]
# curr.next.val = 5 != curr_val = 4
# therefore set prev = curr which is 4
# set curr to next which is 5

# none,1,1,2,3 [3,5]
# curr.next.val = 5 == curr_val = 5
# therefore prev.next (which is 4) is set to curr.next.next which is None
# set curr to next.next which is None

# none,1,1,2,3,3 [5]
# curr.next is None therefore loop
# dummy.next = head

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    if not head.next:
        return head
    
    #to do

        
#delete duplicate nodes
def deleteDuplicates_1(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    if not head.next:
        return head
    
    curr = head
    while curr.next:
        next_val = curr.next.val
        curr_val = curr.val
        if curr_val == next_val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

#[1, 1, 2]
node3 = ListNode(2, None)
node2 = ListNode(1, node3)
node1 = ListNode(1, node2)
result = deleteDuplicates_1(node1)
print(result)