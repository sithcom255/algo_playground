from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result = 0
        root = None
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if root is None:
                    root = Node(nums1[i] + nums2[j])
                else:
                    root.insert(nums1[i] + nums2[j])

        for k in range(len(nums3)):
            for l in range(len(nums4)):
                result += root.search(- (nums3[k] + nums4[l]))
        return result


class Node:
    def __init__(self, value):
        self.value = value
        self.times = 1
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value == self.value:
            self.times += 1
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def search(self, value):
        if value < self.value:
            if self.left is None:
                return 0
            else:
                return self.left.search(value)
        elif value == self.value:
            return self.times
        else:
            if self.right is None:
                return 0
            else:
                return self.right.search(value)


if __name__ == '__main__':
    # nums1 = [1, 2]
    # nums2 = [-2, -1]
    # nums3 = [-1, 2]
    # nums4 = [0, 2]

    nums1 = [0, 1, -1]
    nums2 = [-1, 1, 0]
    nums3 = [0, 0, 1]
    nums4 = [-1, 1, 1]

    print(Solution().fourSumCount(nums1=nums1, nums2=nums2, nums3=nums3, nums4=nums4))
