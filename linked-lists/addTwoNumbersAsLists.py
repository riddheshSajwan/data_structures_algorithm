'''
https://leetcode.com/problems/add-two-numbers/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, A, B):
        new_head = ListNode(-1)
        a = A
        b = B
        curr = new_head
        carry = 0
        while a and b:
            temp_sum = a.val + b.val + carry
            carry = temp_sum//10
            temp_sum %= 10
            curr.next = ListNode(temp_sum)
            curr = curr.next
            a = a.next
            b = b.next
        while a:
            temp_sum = a.val + carry
            carry = temp_sum//10
            temp_sum %= 10
            curr.next = ListNode(temp_sum)
            curr = curr.next
            a = a.next
        while b:
            temp_sum = b.val + carry
            carry = temp_sum//10
            temp_sum %= 10
            curr.next = ListNode(temp_sum)
            curr = curr.next
            b = b.next
        if carry:
            curr.next = ListNode(carry)
        return new_head.next