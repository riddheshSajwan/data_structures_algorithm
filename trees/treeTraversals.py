def _postorder(root):
    if root == None:
        return
    _postorder(root.left)
    _postorder(root.right)
    print(root.val)

def _inorder(root):
    if root == None:
        return
    _inorder(root.left)
    print(root.val)
    _inorder(root.right)
    
def _preorder(root):
    if root == None:
        return
    print(root.val)
    _preorder(root.left)
    _preorder(root.right)