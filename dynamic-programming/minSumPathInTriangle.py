'''
https://leetcode.com/problems/triangle/description/
'''

def minimumTotal(A):
    m = len(A)
    dp = [[0 for j in range(i+2)] for i in range(m+1)]
    for i in range(m-1,-1,-1):
        for j in range(i,-1,-1):
            dp[i][j] = A[i][j] + min(dp[i+1][j],dp[i+1][j+1])
    return dp[0][0]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(triangle))