import random


class RandomizedSet:

    def __init__(self):
        self.random_set = {}
        self.head = None
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.random_set:
            return False
        self.random_set[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.random_set:
            index = self.random_set[val]
            del self.random_set[val]
            dic_val = self.arr[-1]
            if dic_val != val:
                self.random_set[dic_val] = index
            if index == len(self.arr) - 1:
                self.arr.pop()
            else:
                self.arr[index] = self.arr.pop()
            return True
        return False

    def getRandom(self) -> int:
        rand = random.randint(0, len(self.arr) - 1)
        return self.arr[rand]