'''
https://leetcode.com/problems/reverse-nodes-in-k-group/
'''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, head, k):
        head2 = ListNode(head.val)
        head2.next = head
        prev, cur = head2, head2.next
        while cur:
            i = 1
            while cur.next and i != k:
                # move cur.next to prev.next
                prev.next, cur.next.next, cur.next = cur.next, prev.next, cur.next.next
                i += 1     
                if cur.next is None and i < k:
                    # re-reverse end of list
                    cur = prev.next
                    i = k+1
            # move to next group
            prev, cur = cur, cur.next
        return head2.next