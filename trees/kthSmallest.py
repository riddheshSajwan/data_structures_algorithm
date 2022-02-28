'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
'''

def kthSmallest(A, B):    
    def _inorder(root,count,ans):
        if ans != -1:
            return count,ans
        if not root:
            return count,ans
        count,ans = _inorder(root.left,count,ans)
        if count == B and ans == -1:
            ans = root.val
            return count,ans
        if ans != -1:
            return count,ans
        count,ans = _inorder(root.right,count+1,ans)
        return count,ans
    return _inorder(A,1,-1)[1]