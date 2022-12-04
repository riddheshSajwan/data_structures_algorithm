"""
https://www.interviewbit.com/problems/0-1-knapsack/
"""

def knapSack(W, wt, val, n):
    dp = [[0 for x in range(W+1)] for x in range(n+1)]
    # Build table dp[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]],  dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        return knapSack(C,B,A,len(A))

A = [60, 100, 120]
B = [10, 20, 30]
C = 50
print(Solution().solve(A,B,C))