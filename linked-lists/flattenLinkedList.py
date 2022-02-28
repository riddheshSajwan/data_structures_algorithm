'''
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
'''
def flatten(self, head, resumeNode = None):
        
    if not head:
        return None
    
    currentNode = head
    while currentNode:
        prevNode = currentNode
        if currentNode.child:
            childNode = self.flatten(currentNode.child,currentNode.next)
            currentNode.child = None
            currentNode.next = childNode
            childNode.prev = currentNode
        currentNode = currentNode.next
        
    prevNode.next = resumeNode
    if resumeNode:
        resumeNode.prev = prevNode
        
    return head