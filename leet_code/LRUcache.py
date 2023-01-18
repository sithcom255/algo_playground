from typing import List


class LRUCache:
    def __init__(self, capacity: int):
        self.hash_map = {}
        self.head = None
        self.tail = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        self.remove(node)
        node = self.add_to_head(node.key, node.value)
        self.hash_map[key] = node
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.remove(self.hash_map[key])
        elif len(self.hash_map) >= self.capacity:
            tail = self.hash_map.pop(self.tail.key)
            self.remove(tail)
        node = self.add_to_head(key, value)
        self.hash_map[key] = node

    def add_to_head(self, key, value):
        node = Node(key, value)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.right = self.head
            node.right.left = node
            self.head = node
        return node

    def remove_from_tail(self):
        self.tail = self.tail.left
        if self.tail is not None:
            self.tail.right = None

    def remove(self, node):
        l = node.left
        r = node.right
        if l is not None:
            l.right = r
        if r is not None:
            r.left = l
        if node == self.tail:
            self.remove_from_tail()
        if node == self.head:
            self.head = self.head.right
            if self.head is not None:
                self.head.left = None

class Node:
    def __init__(self, key: int, value: int,  left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    lRUCache.get(1)
    lRUCache.put(3, 3)
    lRUCache.get(2)
    lRUCache.put(4, 4)
    lRUCache.get(1)
    lRUCache.get(3)
    lRUCache.get(4)
