'''
https://leetcode.com/problems/partition-list/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, A, B):
        prehead = ListNode(0)
        prehead.next = A
        i,j,prev_j = prehead,A,prehead
        while j:
            #print(i.val,j.val)
            if j.val >= B:
                prev_j = j
                j = j.next
            else:
                if i == prev_j:
                    i = i.next
                    prev_j = j
                    j = j.next
                    continue
                next_i = i.next
                next_j = j.next
                i.next = j
                j.next = next_i
                i = j
                if next_i == A:
                    A = i
                j = next_j
                prev_j.next = j

        return A