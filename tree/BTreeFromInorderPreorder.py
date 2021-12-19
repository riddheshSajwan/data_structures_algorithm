'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def buildTree(A,B):
    root = TreeNode(A[0])
    lst = [root]
    indexMap = {}
    n = len(A)
    for i in range(n):
        indexMap[B[i]] = i
    for i in range(1,n):
        node = TreeNode(A[i])
        rst = ""
        while lst and indexMap[node.val] > indexMap[lst[-1].val]:
            rst = lst.pop()
        if rst:
            rst.right = node
        else:
            lst[-1].left = node
        lst.append(node)
    #print(lst,rst)
    return root 