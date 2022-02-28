'''
https://leetcode.com/problems/balanced-binary-tree/
'''

def ht(node):
    if node == None:
        return -1
    return 1 + max(ht(node.left),ht(node.right))
def isBalanced(A):
    if A == None:
        return 1
    if isBalanced(A.left) and isBalanced(A.right):
        if abs(ht(A.left) - ht(A.right)) < 2:
            return 1
    return 0