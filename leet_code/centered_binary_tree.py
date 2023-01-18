# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        return self.is_symmetric_rec(root.left, root.right)

    def is_symmetric_rec(self, l_node, r_node):
        if l_node is None and r_node is None:
            return True
        if (l_node is None and r_node) or (r_node is None and l_node):
            return False
        if r_node.value != l_node.value:
            return False
        return self.is_symmetric_rec(r_node.left, l_node.right) and \
            self.is_symmetric_rec(l_node.left, r_node.right)
