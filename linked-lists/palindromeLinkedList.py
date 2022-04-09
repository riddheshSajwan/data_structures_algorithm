'''
https://leetcode.com/problems/palindrome-linked-list/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_ll(self,head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def get_mid(self,head):
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    def isPalindrome(self, A):
        mid = self.get_mid(A)
        mid = self.reverse_ll(mid)
        while A and mid:
            if A.val != mid.val:
                return 0
            A = A.next
            mid = mid.next
        return 1