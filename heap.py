class Solution(object):
    def sortArray(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(arr)
        for i in reversed(range(size // 2)):
            self.heap_node(arr, i, size)
        self.get_sorted(arr, size)
        return arr

    def heap_node(self, arr, node, size):
        left = ( node << 1 ) + 1
        right = ( node << 1 ) + 2
        largest = node
        if left < size and arr[left] > arr[node]:
            largest = left
        if right < size and arr[right] > arr[node]:
            largest = right
        if largest != node:
            arr[largest], arr[node] = arr[node], arr[largest]
            self.heap_node(arr, largest, size)

    def get_sorted(self, arr, size):
        while size > 0:
            arr[0], arr[size - 1] = arr[size - 1], arr[0]
            self.heap_node(arr, 0, size)
            size = size - 1
