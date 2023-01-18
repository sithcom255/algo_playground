from typing import Optional

# Definition for a binary tree node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.recursive_pass(root, k)[1]

    def recursive_pass(self, node: TreeNode, k: int):
        intermediary = k
        result = None
        if node.left is not None:
            intermediary, result = self.recursive_pass(node.left, intermediary)
            if result is not None:
                return 0, result
        intermediary -= 1
        if intermediary == 0:
            return 0, node.val
        if node.right is not None:
            intermediary, result = self.recursive_pass(node.right, intermediary)
            if result is not None:
                return 0, result
        return intermediary, result


if __name__ == '__main__':
    root = TreeNode(4, TreeNode(2, TreeNode(0), TreeNode(3)))
    print(Solution().kthSmallest(root, 3))