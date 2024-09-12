from collections import OrderedDict

#Ordered dict acts as a Dictionary and LinkedList combined
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)     
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        
        self.cache[key] = value


obj = LRUCache(2)
# obj.put(1,1)
# obj.put(2,2)
# param_1 = obj.get(1)
# obj.put(3,3)
# param_2 = obj.get(2)
# obj.put(4,4)
# param_3 = obj.get(1)
# param_4 = obj.get(3)
# param_5 = obj.get(4)

#[[2,1],[2,2],[2],[1,1],[4,1],[2]]
# obj.put(2,1)
# obj.put(2,2)
# p1 = obj.get(2)
# obj.put(1,1)
# obj.put(4,1)
# p2 = obj.get(2)
# [[2],[2,6],[1],[1,5],[1,2],[1],[2]]
# p1 = obj.get(2)
# obj.put(2,6)
# p2 = obj.get(1)
# obj.put(1,5)
# obj.put(1,2)
# p3 = obj.get(1)
# p4 = obj.get(2)
# [2,1],[1,1],[2,3],[4,1],[1],[2]
obj.put(2,1)
obj.put(1,1)
obj.put(2,3)
obj.put(4,1)
obj.get(1)
obj.get(2)

