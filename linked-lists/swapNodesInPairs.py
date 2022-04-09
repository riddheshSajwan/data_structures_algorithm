'''
https://leetcode.com/problems/swap-nodes-in-pairs/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, A):
        curr = A
        while curr and curr.next:
            curr.val,curr.next.val = curr.next.val,curr.val
            curr = curr.next.next
        return A