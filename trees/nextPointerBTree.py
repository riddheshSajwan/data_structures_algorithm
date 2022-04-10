'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        def _connect(node):
            if node == None:
                return
            if node.left and node.right:
                node.left.next = node.right
            elif node.left and node.next:
                node.left.next = node.next.left
            if node.right and node.next:
                node.right.next = node.next.left
            _connect(node.left)
            _connect(node.right)
        _connect(root)
        return root
