from typing import List

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_order = {}
        self.hash_map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:


    def put(self, key: int, value: int) -> None:
        if len(self.hash_map) == self.capacity:
            self.hash_map.pop(self.cache_order.pop(-1))
        self.hash_map[key] = value



class Node:
    def __init__(self, value: int, quantity=1):
        self.value = value
        self.quantity = quantity
        self.right = None
        self.left = None

    def insert(self, value):
        nxt = None
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value == self.value:
            self.quantity += 1
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def get_all(self, arr):
        if self.left:
            self.left.get_all(arr)
        arr.append(Node(self.value, quantity=self.quantity))
        if self.right:
            self.right.get_all(arr)


def heapify(arr: List[Node]):
    half = (len(arr) // 2) + 1
    for i in reversed(range(0, half)):
        heap_call(arr, i)


def heap_call(arr: List[Node], i):
    max_elem = i
    left = get_left(i)
    if left < len(arr):
        if arr[max_elem].quantity < arr[left].quantity:
            max_elem = left
    right = get_right(i)
    if right < len(arr):
        if arr[max_elem].quantity < arr[right].quantity:
            max_elem = right
    if max_elem != i:
        arr[i], arr[max_elem] = arr[max_elem], arr[i]
        heap_call(arr, max_elem)


def get_left(i): return i * 2 + 1


def get_right(i): return i * 2 + 2


if __name__ == '__main__':
    print(Solution().topKFrequent(nums=[4,1,-1,2,-1,2,3], k=2))
