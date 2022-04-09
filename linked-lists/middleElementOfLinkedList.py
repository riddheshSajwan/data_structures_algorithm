'''
https://leetcode.com/problems/middle-of-the-linked-list/
'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        if not A or not A.next:
            return A
        i,j = A,A
        while j and j.next:
            i = i.next
            j = j.next.next
        return i.val