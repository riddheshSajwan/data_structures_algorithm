'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(A):
    n = len(A)
    def _buildTree(beg,end):
        if beg < n and beg <= end:
            idx = (beg+end)//2
            node = TreeNode(A[idx])
            node.left = _buildTree(beg,idx-1)
            node.right = _buildTree(idx+1,end)
            return node
    return _buildTree(0,n)