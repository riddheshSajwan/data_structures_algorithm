'''
https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1
'''

def leftView(A):
    res = []
    levels_map = {}
    def _pre(node,level):
        if node == None:
            return
        if level not in levels_map:
            levels_map[level] = node.val
        _pre(node.left,level+1)
        _pre(node.right,level+1)
    _pre(A,0)
    for level in levels_map:
        res.append(levels_map[level])
    return res