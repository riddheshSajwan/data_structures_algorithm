'''
https://leetcode.com/problems/diameter-of-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dia = 0
    def diameterOfBinaryTree(self, A):
        self.dia = 0
        def _dia(node):
            if node is None:
                return -1
            left = _dia(node.left)
            right = _dia(node.right)
            self.dia = max(self.dia,2 + left + right)
            return 1 + max(left,right)
        _dia(A)
        return self.dia