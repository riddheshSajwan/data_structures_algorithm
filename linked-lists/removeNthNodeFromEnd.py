'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_size(self,head):
        res = 0
        curr = head
        while curr:
            res += 1
            curr = curr.next
        return res

    def removeNthFromEnd(self, A, B):
        size = self.find_size(A)
        if size < B:
            B = size
        i = 0
        curr = A
        prev = None
        while i < size - B:
            prev = curr
            curr = curr.next
            i += 1
        if prev is None:
            return A.next
        prev.next = curr.next
        curr.next = None
        return A

