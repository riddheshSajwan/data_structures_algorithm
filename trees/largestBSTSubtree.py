'''
https://practice.geeksforgeeks.org/problems/largest-bst/1#
'''

def largestBst(A):
    #code here
    def _post(node):
        if node is None:
            return
        lst = _post(node.left)
        rst = _post(node.right)
        if lst and rst:
            if (lst[3] < node.data < rst[2]) and (lst[0] and rst[0]):
                return [True, 1 + lst[1] + rst[1], lst[2], rst[3]]
            return [False,max(lst[1],rst[1]),min(lst[2],rst[2],node.data),max(lst[3],rst[3],node.data)] 
        elif lst:
            if node.data > lst[3] and lst[0]:
                return [True, 1+lst[1], lst[2], node.data]
            return [False, lst[1],min(lst[2],node.data),max(lst[3],node.data)]
        elif rst:
            if node.data < rst[2] and rst[0]:
                return [True, 1+rst[1], rst[2], node.data]
            return [False, rst[1],min(rst[2],node.data),max(rst[3],node.data)]
        return [True,1,node.data,node.data]
    return _post(A)[1]