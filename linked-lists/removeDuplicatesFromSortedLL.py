'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, A):
        if A is None:
            return A
        currNode = A
        while currNode.next != None:
            if currNode.val == currNode.next.val :
                currNode.next = currNode.next.next
                continue
            currNode = currNode.next
        return A