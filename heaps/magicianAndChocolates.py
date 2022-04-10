'''
https://www.interviewbit.com/problems/magician-and-chocolates/
'''

import heapq
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        MOD = int(1e9+7)
        res = 0
        for i in range(len(B)):
            B[i] *= -1
        heapq.heapify(B)
        while A > 0:
            temp = -1*heapq.heappop(B)
            res += temp
            heapq.heappush(B,-1*(temp//2))
            A -= 1
        return res%MOD

print(Solution().nchoc(5, [2, 4, 6, 8, 10]))