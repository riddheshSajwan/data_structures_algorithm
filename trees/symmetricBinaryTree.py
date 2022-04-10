'''
https://leetcode.com/problems/symmetric-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    nodes_map = {}

    def preorder(self,node,level):
        if level not in self.nodes_map:
            self.nodes_map[level] = []
        if node is None:
            self.nodes_map[level].append(None)
            return
        self.nodes_map[level].append(node.val)
        self.preorder(node.left,level+1)
        self.preorder(node.right,level+1)
    def isSymmetric(self, root):
        self.nodes_map = {}
        self.preorder(root,0)
        for level in self.nodes_map:
            if self.nodes_map[level] != self.nodes_map[level][::-1]:
                return False
        return True