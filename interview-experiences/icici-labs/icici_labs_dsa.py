''' Question:
Paul has a set of unique numbers. He wants to store numbers in a binary tree such that
whenever a number is given, he can exactly tell how many numbers are less than the given
number.
Help Paul by coding the logic in your language of choice without using any libraries for tree
implementation.
Evaluation Criteria:
1. Well written code in your language of choice
2. Time & Space complexities (How efficient is your code?)
3. Alternate approaches (Different ways of solving the problem)
'''

''' Answer:
Assumption - n is the unique numbers Paul has in the beginning. 

We can solve this question by:
1. Storing these numbers in a binary search tree, wherein a left child will be smaller than its parent and a right child will be greater than its parent.
2. Then we can store the inorder traversal of this tree in an array. 
3. Now, to find the count of numbers lesser than a given number, we can perform a traversal in binary search fashion. 

Time complexity - O(n^2 + n + logn) ~ O(n^2)  |  (n^2 for build BST (worst case), n to find the inorder and logn is to find the count of numbers lesser than a given number)
Space Complexity - O(n) | (to store the inorder array)

Alternate Approach :
1. We can simply use an AVL tree (height-balanced binary tree) in which creation of AVL will take O(nlogn) time where logn is insertion time for every element.
OR
2. We can sort the numbers in advance and then create BST from it by always taking the middle of array in O(nlogn + n) time. (nlogn to sort and n to build BST)
'''

# Assumption - nums is the initial array of integers that Paul hasānd number is the given number for which we have to find the count of lesser numbers.

class Node:

    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def insert(self,root,node):
        if root is None:
            return node
        if root.val < node.val:
            root.right = self.insert(root.right, node)
        else:
            root.left = self.insert(root.left, node)
        return root

    def build_bst(self,nums):
        if nums == []:
            return None
        root = Node(nums[0])
        for i in range(1,len(nums)):
            root = self.insert(root,Node(nums[i]))
        return root

    def inorder_traversal(self,root,res):
        if root is None:
            return res
        res = self.inorder_traversal(root.left,res)
        res.append(root.val)
        res = self.inorder_traversal(root.right,res)
        return res

    def find_lesser(self,nums,number):
        beg,end = 0,len(nums)-1
        while beg <= end:
            mid = beg + (end-beg)//2
            if nums[mid] == number:
                return mid
            elif nums[mid] > number:
                end = mid-1
            else:
                beg = mid+1
        return mid+1

    def solve(self,nums,number):
        root = self.build_bst(nums)
        inorder = self.inorder_traversal(root,[])
        return self.find_lesser(inorder, number)

print(Solution().solve([3,1,34,67,23,45,69], 53))