class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        root = None
        for i, num in enumerate(nums):
            if root is None:
                root = Node(num, i)
                continue
            found = root.search(target - num)
            if found:
                return [i, found.index]
            else:
                root.insert(num, i)

# this need to be self-balancing
class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.left = None
        self.right = None

    def search(self, value):
        if self.value == value:
            return self
        if value < self.value and self.left:
            return self.left.search(value)
        if value > self.value and self.right:
            return self.right.search(value)

    def insert(self, value, index):
        if value < self.value:
            if self.left:
                self.left.insert(value, index)
            else:
                self.left = Node(value, index)
        if value > self.value:
            if self.right:
                self.right.insert(value, index)
            else:
                self.right = Node(value, index)
