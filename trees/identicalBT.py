'''
https://leetcode.com/problems/same-tree/
'''

def isSameTree(A,B) -> bool:
    def _isSame(node1,node2):
        if node1 == None and node2 == None:
            return 1
        if node1  == None or node2 == None:
            return 0
        return (node1.val == node2.val) and _isSame(node1.left,node2.left) and _isSame(node1.right,node2.right)
    return _isSame(A,B)