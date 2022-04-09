'''
https://leetcode.com/problems/merge-two-sorted-lists/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, A, B):
        new_head = ListNode(-1)
        curr = new_head
        curr_A,curr_B = A,B
        while curr_A and curr_B:
            if curr_A.val <= curr_B.val:
                curr.next = curr_A
                temp = curr_A.next
                curr_A.next = None
                curr_A = temp
            else:
                curr.next = curr_B
                temp = curr_B.next
                curr_B.next = None
                curr_B = temp
            curr = curr.next
        if curr_A:
            curr.next = curr_A
        if curr_B:
            curr.next = curr_B
        return new_head.next