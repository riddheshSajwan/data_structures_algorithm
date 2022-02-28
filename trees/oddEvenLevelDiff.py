'''
https://practice.geeksforgeeks.org/problems/odd-even-level-difference/1
'''

def getLevelDiff(A):
    # Code here
    def _pre(node,level,res):
        if node == None:
            return res
        res -= (-1)**(level%2)*node.data
        res = _pre(node.left,level+1,res)
        res = _pre(node.right,level+1,res)
        return res
    return _pre(A,1,0)