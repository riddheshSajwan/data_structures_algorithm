class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None

class doublyLinkedList():

    def __init__(self,node=None):
        self.head = node
        self.tail = self.head
        self.length = 1
    
    def append(self,node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.length += 1
        
    def preprend(self,node):
        node.next = self.head
        self.head.prev = node
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
        currentNode.next.prev = node
        node.next = currentNode.next
        node.prev = currentNode
        currentNode.next = node
        self.length += 1

    def access(self,index):
        currentNode = self.traverseToIndex(index)
        return currentNode.next.value
    
    def remove(self,index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return
        currentNode = self.traverseToIndex(index)
        nodeToDelete = currentNode.next  
        if nodeToDelete == self.tail:
            self.tail = currentNode
            self.tail.next = None
            self.length -= 1
            return      
        currentNode.next = nodeToDelete.next
        nodeToDelete.next.prev = currentNode
        self.length -= 1
    
    def reverse(self):
        prevNode = self.head
        currentNode = self.head.next
        self.head.next = None
        self.head.prev = self.tail.prev
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prevNode
            currentNode.prev = nextNode
            prevNode = currentNode
            currentNode = nextNode
        self.tail = prevNode
        self.head = self.tail

    def printReverse(self):
        dll = ''
        currentNode = self.tail
        while currentNode.prev:
            dll += str(currentNode.value) + '<->'
            currentNode = currentNode.prev
        dll += str(currentNode.value)
        print(dll)

    def printList(self):
        dll = ''
        currentNode = self.head
        while currentNode.next:
            dll += str(currentNode.value) + '<->'
            currentNode = currentNode.next
        dll += str(currentNode.value)
        print(dll)

myLinkedList = doublyLinkedList(Node(24))
myLinkedList.append(Node(25))
myLinkedList.preprend(Node(23))
myLinkedList.insert(2,Node(35))
myLinkedList.printList()
myLinkedList.printReverse()
myLinkedList.reverse()
myLinkedList.printList()
print(myLinkedList.access(2))
myLinkedList.remove(2)
myLinkedList.printList()