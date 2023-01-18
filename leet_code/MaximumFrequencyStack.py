from typing import List
from collections import OrderedDict


# musi to trackovat kolik elementu je na stacku
# kdyz prijde novy element
# podivam se jestli je to v dic,
# pokud to tam je:
#   tak si vezmu node, a pushnu do stacku hodnotu s velikosti stacku
# pokud to tam neni:
#   pushnu dalsi velikost, pridam do arr element, switchnu s topem
#
#

class FreqStack:
    def __init__(self):
        self.heap = []
        self.height = 0
        self.root = None
        self.map = {}
        self.should_heap = False

    def pop(self) -> int:

        # get max frequency from heap
        # pop height and the indexex arr in node
        # heap_pop to ensure max heap
        # check if map is empty and remove
        if not self.heap:
            return -1
        if self.should_heap:
            self.heapify()
        self.print("pop", "")
        node = self.heap[0]
        node.indices.pop()
        node.prio -= 1
        final_index = self.heapify_pop(0)
        if not node.indices:
            del self.map[node.key]
            self.heap[final_index], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[
                final_index]
            self.heap.pop()
            self.heapify_put(final_index)
        # self.height -= 1

        return node.key

    def push(self, key: int) -> None:
        # check if in map
        # append to new index if so
        # run heapify to ensure max heap
        # increment height
        node = None
        if key in self.map:
            node = self.map[key]
            node.prio += 1
            node.indices.append(self.height)
            self.height += 1
            self.should_heap = True
        else:
            node = Node(key)
            self.map[key] = node
            self.heap.append(node)
            node.indices.append(self.height)
            self.height += 1
            self.heapify_put(len(self.heap) - 1)
        self.print("push", key)

    def print(self, operation, key):
        # print(operation, key, " (", end="")
        # for elem in self.heap:
        #     print("(", elem.key, "-", elem.prio, "-", elem.indices, ") ", end="")
        # print(")")
        pass

    def heapify_put(self, child):
        index = self.get_parent(child)
        if index < 0:
            return
        l = self.get_left(index)
        r = self.get_right(index)
        max_index = index
        if l:
            max_index = self.max_index(l, max_index)
        if r:
            max_index = self.max_index(r, max_index)
        if max_index != index:
            self.heap[max_index], self.heap[index] = self.heap[index], self.heap[max_index]
            self.heapify_put(index)

    def heapify(self):
        for i in reversed(range(len(self.heap) // 2)):
            self.heapify_pop(i)

    def heapify_pop(self, index):
        l = self.get_left(index)
        r = self.get_right(index)
        max_index = index
        if l:
            max_index = self.max_index(l, max_index)
        if r:
            max_index = self.max_index(r, max_index)
        if max_index != index:
            self.heap[max_index], self.heap[index] = self.heap[index], self.heap[max_index]
            return self.heapify_pop(max_index)
        return index

    def max_index(self, other, max_index):
        max_node = self.heap[max_index]
        node = self.heap[other]
        if node.prio > max_node.prio \
                or node.prio == max_node.prio and node.indices[-1] > max_node.indices[-1]:
            return other
        return max_index

    def get_parent(self, index):
        parent_index = 0
        if index > 0 and index % 2 == 1:
            parent_index = index // 2
        elif index > 0:
            parent_index = index // 2 - 1
        return parent_index

    def get_left(self, index):
        l_index = index * 2 + 1
        if l_index < len(self.heap):
            return l_index
        return None

    def get_right(self, index):
        r_index = index * 2 + 2
        if r_index < len(self.heap):
            return r_index
        return None


class Node:
    def __init__(self, key: int, prio=1, left=None, right=None):
        self.key = key
        self.prio = prio
        self.indices = []
        self.left = left
        self.right = right


def test(input, params, expected):
    freqStack = FreqStack()
    for i, action in enumerate(input):
        match action:
            case "push":
                freqStack.push(params[i][0])
                res.append(None)
            case "pop":
                res.append(freqStack.pop())
            case other:
                res.append(None)
    assert res == expected


def test1():
    global input, params, res, expected
    input = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "push", "pop", "push", "pop", "push",
             "pop", "push", "pop", "pop", "pop", "pop", "pop", "pop"]
    params = [[], [4], [0], [9], [3], [4], [2], [], [6], [], [1], [], [1], [], [4], [], [], [], [], [], []]
    res = []
    expected = [None, None, None, None, None, None, None, 4, None, 6, None, 1, None, 1, None, 4, 2, 3, 9, 0, 4]
    test(input, params, expected)


def test16():
    global input, params, res, expected
    input = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "push", "pop", "push", "pop", "push",
             "pop", "push", "pop", "pop", "pop", "pop", "pop", "pop"]

    params = [[], [7], [6], [2], [6], [3], [3], [], [2], [], [2], [], [5], [], [6], [], [], [], [], [], []]

    res = []
    expected = [None, None, None, None, None, None, None, 3, None, 2, None, 2, None, 6, None, 6, 5, 3, 2, 6, 7]
    test(input, params, expected)


if __name__ == '__main__':
    test1()
    test16()
