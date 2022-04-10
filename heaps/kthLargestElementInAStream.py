'''
https://practice.geeksforgeeks.org/problems/kth-largest-element-in-a-stream2220/1/
'''
from heapq import heapify,heappush,heappop 
class Solution:
    def kthLargest(self, A, B, n):
        # code here 
        if len(B) < A:
            return [-1 for i in range(len(B))]
        res = [-1]*(A-1)
        minheap = [B[i] for i in range(A)]
        heapify(minheap)
        idx = A
        while True:
            res.append(minheap[0])
            if idx == len(B):
                break
            if B[idx] > minheap[0]:
                heappush(minheap,B[idx])
                heappop(minheap)
            idx += 1
        return res

print(Solution().kthLargest(2, [15, 20, 99, 1], 4))