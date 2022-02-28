'''
https://leetcode.com/problems/linked-list-cycle/
'''
def hasCycle(self, head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
      
      
def hasCycle2(self, head):
    cache = {}
    index = 0
    currentNode = head
    while currentNode:
        if currentNode in cache:
            return True
        cache.update({currentNode:index})
        currentNode = currentNode.next
        index += 1
    return False