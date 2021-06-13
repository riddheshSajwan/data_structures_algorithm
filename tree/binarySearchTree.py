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

# find method for bst.
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

    def countNodes(self):
        if not self.root:
            return 0
        def _countNodes(currentNode):
            if currentNode.left and currentNode.right:
                return 1 +  _countNodes(currentNode.left) + _countNodes(currentNode.right)
            elif currentNode.right:
                return 1 + _countNodes(currentNode.right)
            elif currentNode.left:
                return 1 + _countNodes(currentNode.left)
            return 1
        return _countNodes(self.root)

# find method for any binary tree
    def findRecursive(self,value):
        if self.root.value == value:
            return True
        def _findRecusrsive(currentNode):
            if currentNode.value == value:
                return True
            elif currentNode.right and currentNode.left:
                return _findRecusrsive(currentNode.left) or _findRecusrsive(currentNode.right)
            elif currentNode.right:
                return _findRecusrsive(currentNode.right)
            elif currentNode.left:
                return _findRecusrsive(currentNode.left)
            return False
        return _findRecusrsive(self.root)

   #assuming root to be at height 1.  
    def maxDepth(self):
        if not self.root:
            return 0
        def _maxDepth(currentNode,height=0):
            if currentNode == self.root:
                height = 1
            if currentNode.right and currentNode.left:
                return height + max(_maxDepth(currentNode.left,height),_maxDepth(currentNode.right,height))
            elif currentNode.right:
                return height + _maxDepth(currentNode.right,height)
            elif currentNode.left:
                return height + _maxDepth(currentNode.left,height)
            return height
        return _maxDepth(self.root)

myTree = binarySearchTree(Node(23))
myTree.insert(Node(15))
myTree.insert(Node(14))
myTree.insert(Node(16))
myTree.insert(Node(24))
myTree.insert(Node(23))
print(myTree.find(69))
print(myTree.countNodes())
print(myTree.findRecursive(14))
print(myTree.maxDepth())