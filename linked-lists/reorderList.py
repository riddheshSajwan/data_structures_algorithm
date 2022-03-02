'''
https://leetcode.com/problems/reorder-list/
'''

def reorderList(A):
    node_map = {}
    curr = A
    i = 0
    while curr:
        node_map[i] = curr
        curr = curr.next
        i += 1
    start,end = 0,i-1
    while start < end :
        temp = node_map[start].next
        node_map[start].next = node_map[end]
        node_map[end].next = temp
        start += 1
        end -= 1
    node_map[start].next = None
    return A