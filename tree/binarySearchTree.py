class Node:
    def __init__(self,value=None):
        self.left = None
        self.right = None
        self.value = value

class binarySearchTree:
    def __init__(self,node=None):
        self.root = node

    def insert(self,node):
        currentNode = self.root
        while True:
            if node.value < currentNode.value:
                if currentNode.left:
                    currentNode = currentNode.left
                else:
                    currentNode.left = node
                    return     
            else:
                if currentNode.right:
                    currentNode = currentNode.right
                else:
                    currentNode.right = node   
                    return       

    def find(self,value):
        currentNode = self.root
        while True:
            if value < currentNode.value:
                if currentNode.left:
                    currentNode = currentNode.left
                else:
                    return False    
            elif value > currentNode.value:
                if currentNode.right:
                    currentNode = currentNode.right
                else:
                    return False
            else:
                return True


myTree = binarySearchTree(Node(23))
myTree.insert(Node(15))
myTree.insert(Node(14))
myTree.insert(Node(16))
myTree.insert(Node(24))
myTree.insert(Node(23))
print(myTree.find(69))
