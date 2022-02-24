'''
https://leetcode.com/problems/binary-tree-right-side-view/
'''

def rightSideView(A):
    levelMap = {}
    def _pre(node,level):
        if node == None:
            return
        levelMap[level] = node.val
        _pre(node.left,level+1)
        _pre(node.right,level+1)
    _pre(A,0)
    res = []
    #print(dist_arr)
    for item in levelMap:
        res.append(levelMap[item])
    return res