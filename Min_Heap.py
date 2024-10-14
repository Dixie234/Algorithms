class Heap:
    def __init__(self):
        self.data = []

    @property
    def root(self):
        return self.data[0]
    
    @property
    def last(self):
        return self.data[-1]
    
    def left_child_index(self, index):
        return (index * 2) + 1
    
    def right_child_index(self, index):
        return (index * 2) + 2
    
    def parent_index(self, index):
        return (index - 1) >> 1
    
    def insert(self, value) -> None:
        self.data.append(value)
        _siftdown(self.data, 0, len(self.data) - 1)

    def delete(self):
        self.data[0] = self.data.pop()
        trickle_node_index = 0

        while self.has_greater_child(trickle_node_index):
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)
            self.data[trickle_node_index], self.data[larger_child_index] = self.data[larger_child_index], self.data[trickle_node_index]

            trickle_node_index = larger_child_index

    def has_greater_child(self, index):
        val = self.data[index]
        left_val = self.data[self.left_child_index(index)]
        right_val = self.data[self.right_child_index(index)]

        return (left_val and left_val > val) or (right_val and right_val > val)
    
    def calculate_larger_child_index(self, index):
        left_index = self.left_child_index(index)
        left_val = self.data[left_index]
        right_index = self.right_child_index(index)
        right_val = self.data[right_index]

        if not right_val:
            return left_index
        
        if right_val > left_val:
            return right_index
        else:
            return left_index

def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem