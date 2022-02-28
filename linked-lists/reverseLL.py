'''
https://leetcode.com/problems/reverse-linked-list/
'''
# using recursive approach
def reverseList(self, head, prevNode = None):
    if not head:
        return None
    currentNode = head.next
    head.next = prevNode
    prevNode = head
    if currentNode:
        head = self.reverseList(currentNode,prevNode)
    else:
        head = prevNode
    return head

# using iterative approach
def reverseList2(self, head, prevNode = None):
    if not head:
        return None
    currentNode = head.next
    prevNode = head
    head.next = None
    while currentNode:
        temp = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = temp
    head = prevNode
    return head
        