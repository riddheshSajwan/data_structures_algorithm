class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class singlyLinkedList():

    def __init__(self,node=None):
        self.head = node
        self.tail = self.head
        self.length = 1
    
    def append(self,node):
        self.tail.next = node
        self.tail = node
        self.length += 1
        
    def preprend(self,node):
        node.next = self.head
        self.head = node
        self.length += 1

    def traverseToIndex(self,index):
        if index >= self.length or index < 0:
            raise Exception("Index out of bound")
        currentNode = self.head
        while index-1 > 0:
            currentNode = currentNode.next
            index -= 1
        return currentNode
    
    def insert(self,index,node):
        if index == 0:
            self.preprend(node)
            return
        currentNode = self.traverseToIndex(index)
        node.next = currentNode.next
        currentNode.next = node
        self.length += 1

    def access(self,index):
        currentNode = self.traverseToIndex(index)
        return currentNode.next.value
    
    def remove(self,index):
        
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        currentNode = self.traverseToIndex(index)
        nodeToDelete = currentNode.next 
        if nodeToDelete == self.tail:
            self.tail = currentNode
        currentNode.next = nodeToDelete.next
        self.length -= 1

    def reverse(self):
        if self.length == 1:
            return
        prevNode = self.head
        currentNode = self.head.next
        self.head.next = None
        self.tail = self.head
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        self.head = prevNode
             

    def printList(self):
        sll = ''
        currentNode = self.head
        while currentNode.next:
            sll += str(currentNode.value) + '->'
            currentNode = currentNode.next
        sll += str(currentNode.value)
        print(sll)

myLinkedList = singlyLinkedList(Node(24))
myLinkedList.append(Node(25))
myLinkedList.preprend(Node(23))
myLinkedList.insert(1,Node(35))
myLinkedList.printList()
myLinkedList.reverse()
myLinkedList.printList()
print(myLinkedList.access(2))
myLinkedList.remove(2)
myLinkedList.printList()