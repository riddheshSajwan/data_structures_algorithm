'''
https://leetcode.com/problems/invert-binary-tree/
'''
class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root