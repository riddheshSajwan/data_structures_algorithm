'''
https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
'''

import heapq
class Solution:
    def largestSumAfterKNegations(self, A, B):
        heapq.heapify(A)
        while B > 0:
            heapq.heappush(A,-1*heapq.heappop(A))
            B -= 1
        return sum(A)
    
A = [3,-1,0,2]
B = 3
print(Solution().largestSumAfterKNegations(A, B))
