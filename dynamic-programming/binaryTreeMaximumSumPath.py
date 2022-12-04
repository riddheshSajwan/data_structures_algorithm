'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/892082369/
'''

class Solution:
    def maxPathSum(self, root):
        self.global_maximum = root.val
        
        def postorder(root):
            
            # root check
            if not root:
                return 0
            
            if not root.left and not root.right:
                self.global_maximum = max(self.global_maximum, root.val)
                return root.val
            
            # postorder part
            left = postorder(root.left)
            right = postorder(root.right)
            
            # actions
            local_maximum = max(left + root.val, right + root.val, root.val)
            self.global_maximum = max(self.global_maximum, local_maximum, left + root.val + right)
            return local_maximum
        
        
        postorder(root)
        return self.global_maximum