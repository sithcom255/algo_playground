from typing import List, Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        one = TreeNode(0)
        three = TreeNode(0, TreeNode(0), TreeNode(0))
        dp = {1 : [one], 3 : [three]}

    def all_posible_rec(self, n, dp):
        if n in dp:
            return dp[n]
        result = []
        # kombinace
        if n +

if __name__ == '__main__':
