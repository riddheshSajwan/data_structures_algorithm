'''
Problem Description
Given two BST's A and B, return the (sum of all common nodes in both A and B) % (109 +7) .
In case there is no common node, return 0.

NOTE:
Try to do it one pass through the trees.

Problem Constraints
1 <= Number of nodes in the tree A and B <= 105
1 <= Node values <= 106

Input Format
First argument represents the root of BST A.
Second argument represents the root of BST B.

Output Format
Return an integer denoting the (sum of all common nodes in both BST's A and B) % (109 +7) .

Example Input
Input 1:
 Tree A:
    5
   / \
  2   8
   \   \
    3   15
        /
        9
 Tree B:
    7
   / \
  1  10
   \   \
    2  15
       /
      11

Input 2:
  Tree A:
    7
   / \
  1   10
   \   \
    2   15
        /
       11

 Tree B:
    7
   / \
  1  10
   \   \
    2  15
       /
      11


Example Output
Output 1:
 17
Output 2:
 46


Example Explanation

Explanation 1:
 Common Nodes are : 2, 15
 So answer is 2 + 15 = 17
Explanation 2:
 Common Nodes are : 7, 2, 1, 10, 15, 11
 So answer is 7 + 2 + 1 + 10 + 15 + 11 = 46
 '''

class Solution:

    cache = set()
    res = 0
    MOD = int(1e9+7)

    def _pre(self,root):
        if root == None:
            return
        #print(root.val)
        if root.val in self.cache:
            self.res = (self.res + root.val)%self.MOD
        else:
            self.cache.add(root.val)
        self._pre(root.left)
        self._pre(root.right)

    def solve(self, A, B):
        self.cache = set()
        self.res = 0
        self._pre(A)
        #print(self.cache,len(self.cache))
        self._pre(B)
        return self.res%self.MOD