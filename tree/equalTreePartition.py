'''
https://leetcode.com/problems/equal-tree-partition/
'''
'''
https://www.geeksforgeeks.org/check-if-removing-an-edge-can-divide-a-binary-tree-in-two-halves/
'''

def solve(A):

    def _sum(node):
        if node == None:
            return 0
        return node.val + _sum(node.left) + _sum(node.right)

    tree_sum = _sum(A)
    if tree_sum % 2 == 1:
        return 0

    def subtree_sum(node):
        if node == None:
            return (0,False)
        lst = subtree_sum(node.left)
        if lst[1]:
            return (0,True)
        rst = subtree_sum(node.right)
        if rst[1]:
            return (0,True)
        if lst and rst:
            sub_sum = node.val + lst[0] + rst[0]
        elif lst:
            sub_sum = node.val + lst[0]
        elif rst:
            sub_sum = node.val + rst[0]
        else:
            sub_sum = node.val
        if sub_sum == tree_sum//2 and not (tree_sum == 0 and node == A):
            return (sub_sum,True)
        return (sub_sum,False)
        
    return int(subtree_sum(A)[1])