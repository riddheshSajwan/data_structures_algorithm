'''
https://practice.geeksforgeeks.org/problems/sum-tree/1
'''

def isSumTree(A):
    cache = {None:0}
    def sumBT(node):
        if node in cache:
            return cache[node]
        cache[node] = node.data + sumBT(node.left) + sumBT(node.right)
        return cache[node]
    sumBT(A)
    def _isSumTree(node):
        if node == None or (node.left == None and node.right == None):
            return 1
        return int(node.data == cache[node.left] + cache[node.right] and _isSumTree(node.left) and _isSumTree(node.right))
    return _isSumTree(A)