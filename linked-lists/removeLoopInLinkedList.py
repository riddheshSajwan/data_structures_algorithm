'''
https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1/#
'''
'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def get_intersection_point(self,head):
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
    def get_last_node(self,head):
        curr = head.next
        while curr.next != head:
            curr = curr.next
        return curr
    def removeLoop(self, A):
        # code here
        # remove the loop without losing any nodes
        intersection_point = self.get_intersection_point(A)
        pointer_1,pointer_2 = A, intersection_point
        prev = None
        while pointer_1 and pointer_2:
            if pointer_1 == pointer_2:
                if prev is None:    
                    prev = self.get_last_node(A)
                prev.next = None
                return A
            prev = pointer_2
            pointer_1,pointer_2 = pointer_1.next, pointer_2.next
        return A