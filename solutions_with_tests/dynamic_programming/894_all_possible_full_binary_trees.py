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
        self.all_posible_rec(n, dp)
        return dp[n]

    def all_posible_rec(self, n, dp):
        if n in dp:
            return dp[n]
        result = []
        for key in range(n):
            if key > n:
                break
            if key not in dp:
                self.all_posible_rec(key, dp)
            if n - 1 - key in dp:
                result.extend(self.combine(dp[key], dp[n - key - 1]))
            else:
                self.all_posible_rec(n - 1 - key, dp)
                result.extend(self.combine(dp[key], dp[n - key - 1]))
        dp[n] = result

    def combine(self, first, second):
        result = []
        for node_f in first:
            for node_s in second:
                result.append(TreeNode(0, node_s, node_f))
                # result.append(TreeNode(0, node_f, node_s))
        return result


if __name__ == '__main__':
    print(Solution().allPossibleFBT(7))
