import random


class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        before = len(self.set)
        self.set.add(val)
        after = len(self.set)
        if before != after:
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        try:
            self.set.remove(val)
            return True
        except:
            return False   

    def getRandom(self) -> int:
        length = len(self.set)
        index = random.randint(0, length - 1)
        set_list = list(self.set)
        return set_list[index]
