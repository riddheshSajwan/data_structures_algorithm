'''
https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1#
'''

import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,A,n) :
        heapq.heapify(A)
        res = 0
        while n > 1:
            res_temp = heapq.heappop(A) + heapq.heappop(A)
            heapq.heappush(A,res_temp)
            n -= 1
            res += res_temp
        return res

print(Solution().minCost([4, 3, 2, 6], 4))