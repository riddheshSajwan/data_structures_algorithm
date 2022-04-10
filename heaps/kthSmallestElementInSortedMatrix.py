'''
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
'''

from heapq import heappush,heappop,heapify
class Solution:
    def kthSmallest(self, A, B):
        n,m=len(A),len(A[0])
        minheap = []
        for row in range(n):
            heappush(minheap,(A[row][0],row,0))
        for i in range(B):
            res,row,col = heappop(minheap)
            if col+1 < m:
                heappush(minheap, (A[row][col+1], row, col+1))
        return res 

A = [[1,5,9],[10,11,13],[12,13,15]]
B = 8
print(Solution().kthSmallest(A, B))