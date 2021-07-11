'''
https://leetcode.com/problems/linked-list-cycle-ii/
'''
def detectCycle(self, head):
    currentNode = head
    while currentNode:
        if currentNode.val == float('-inf'):
            return currentNode
        currentNode.val = float('-inf')
        currentNode = currentNode.next
    return None
      
def detectCycle2(self, head):
    cache = set()
    currentNode = head
    while currentNode:
        if currentNode in cache:
            return currentNode
        cache.add(currentNode)
        currentNode = currentNode.next
    return None
    