'''
https://leetcode.com/problems/path-sum/
'''

def hasPathSum(A, B):
    if A == None:
        return 0
    B -= A.val
    if A.left == None and A.right == None:
        return int(B == 0)
    return hasPathSum(A.left,B) or hasPathSum(A.right,B)