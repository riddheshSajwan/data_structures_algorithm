'''
https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1
'''

def topView(A):
    res = []
    widthMap = {}
    def _trav(node,dist,level):
        if node == None:
            return
        if dist not in widthMap:
            widthMap[dist] = (node.val,level)
        elif level < widthMap[dist][1]:
            widthMap[dist] = (node.val,level)
        _trav(node.left,dist+1,level+1)
        _trav(node.right,dist-1,level+1)
    _trav(A,0,0)
    for dist in widthMap:
        res.append(widthMap[dist][0])
    return res