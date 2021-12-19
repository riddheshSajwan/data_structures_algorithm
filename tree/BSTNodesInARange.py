'''
https://practice.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1
'''

def solve(A, B, C):
    def _pre(node,count):
        if node  == None:
            return count
        if B <= node.val <= C:
            count += 1
        count = _pre(node.left,count)
        count = _pre(node.right,count)
        return count
    return _pre(A,0)

# Better Solution
def solveBetter(A, B, C):
    if not A:
        return 0
    if A.val < B:
        return solveBetter(A.right, B, C)
    if A.val > C:
        return solveBetter(A.left, B, C)
    return 1 + solveBetter(A.left, B, C) + solveBetter(A.right, B, C)