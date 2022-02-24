'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

def levelOrder(A):
    queue = [A]
    idx = 0
    res = []
    qlen = 1
    while idx < qlen:
        level = []
        for i in range(idx,qlen):
            level.append(queue[i].val)
        res.append(level)
        for i in range(idx,qlen):
            currNode = queue[i]
            if currNode.left:
                queue.append(currNode.left)
                qlen += 1
            if currNode.right:
                queue.append(currNode.right)
                qlen += 1
            idx += 1
    return res
