'''
https://leetcode.com/problems/validate-binary-search-tree/
'''

# my solution
def isValidBST(self, root):

    current_node = root
    if not current_node:
        return False
    lowest, highest = float('-inf'), float('inf')

    def is_bst(node, lowest, highest):
        if not node.left and not node.right:
            return True
        elif node.left and node.right:
            if lowest < node.left.val < node.val and node.val < node.right.val < highest:
                return is_bst(node.left, lowest, node.val) and is_bst(node.right, node.val, highest)
        elif node.left and lowest < node.left.val < node.val:
            return is_bst(node.left, lowest, node.val)
        elif node.right and node.val < node.right.val < highest:
            return is_bst(node.right, node.val, highest)
        return False

    return is_bst(current_node, lowest, highest)

# cleaner solution
def isValidBST2(self, root):

    def is_BST(tree, low_range=float("-inf"), high_range=float("inf")):
      if not tree:
          return True
      elif not low_range < tree.val < high_range:
          return False
      return (is_BST(tree.left, low_range, tree.val) and
              is_BST(tree.right, tree.val, high_range))

    return is_BST(root)

# Best solution
def isValidBST3(self, root):
  S = []
  cur = root
  lastVal = -float('inf')
  while True:
    if cur:
        S.append(cur)
        cur = cur.left
    else:
        cur = S.pop()
        if cur.val <= lastVal:
            return False
        lastVal = cur.val
        cur = cur.right
    if not cur and not S:
        break

  return True
