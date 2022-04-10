'''
https://practice.geeksforgeeks.org/problems/min-distance-between-two-given-nodes-of-a-binary-tree/1/#
'''

#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:

    ans = -1
    visited = set()
    
    def get_parent_map(self,node,parent,parent_map):
        if node is None:
            return parent_map
        if parent:
            parent_map[node] = parent
        parent_map = self.get_parent_map(node.left,node,parent_map)
        parent_map = self.get_parent_map(node.right,node,parent_map)
        return parent_map

    def dfs(self,node,parent_map,target,dist):
        if node is None or node in self.visited or self.ans != -1:
            return
        if node.data == target:
            self.ans = dist
            return
        self.visited.add(node)
        if node in parent_map:
            self.dfs(parent_map[node],parent_map,target,dist+1)
        self.dfs(node.left,parent_map,target,dist+1)
        self.dfs(node.right,parent_map,target,dist+1)

    def findDist(self,A,B,C):
        self.ans = -1
        self.visited = set()
        parent_map = self.get_parent_map(A,None,{A:None})
        for node in parent_map:
            if node.data == B:
                #print(node.val,B)
                self.dfs(node,parent_map,C,0)
                break
        return self.ans