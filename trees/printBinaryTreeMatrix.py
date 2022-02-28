'''
https://leetcode.com/problems/print-binary-tree/
'''

def printTree(self, root):
  if not root:
        return 0
  def _maxDepth(currentNode,height=0):
    if currentNode == root:
        height = 0
    if currentNode.right and currentNode.left:
        return height + max(_maxDepth(currentNode.left,height),_maxDepth(currentNode.right,height)) + 1
    elif currentNode.right:
        return height + _maxDepth(currentNode.right,height) + 1
    elif currentNode.left:
        return height + _maxDepth(currentNode.left,height) + 1
    return height
      
  height = _maxDepth(root)
  #print(height)
  row,column = height+1,pow(2,height+1)-1
  res = [["" for i in range(column)] for i in range(row)]
  #print(root.val)
  def fillMatrix(currentNode,row,beg,end):
    if not currentNode:
      return res
    index = (beg+end)//2
    #print(row)
    #print(index)
    res[row][index]=str(currentNode.val)
    #print(res)
    if currentNode.left:
      fillMatrix(currentNode.left,row+1,beg,index-1)
    if currentNode.right:
      fillMatrix(currentNode.right,row+1,index+1,end)
    return res
  return fillMatrix(root,0,0,column-1)