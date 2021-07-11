'''
https://leetcode.com/problems/reverse-linked-list-ii/
'''

def reverseBetween(self, head, left, right):
    if left == right:
        return head
    index = 1
    currentNode = head
    while index <= right:
        temp = currentNode.next
        if index == left-1:
            leftPrevNode = currentNode
        elif index == left:
            leftNode = currentNode
            prevNode = currentNode
        elif index == right:
            rightNode = currentNode
        if left != 1:
            leftPrevNode.next = rightNode
        if index > left:
            currentNode.next = prevNode
            prevNode = currentNode
        currentNode = temp
        index += 1
    leftNode.next = currentNode
    
    if left == 1:
        return rightNode
    return head