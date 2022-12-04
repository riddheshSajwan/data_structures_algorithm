'''
https://leetcode.com/problems/minimum-path-sum/description/
'''

def minPathSum(A):
    m = len(A)
    n = len(A[0])
    dp = [[0]*n for i in range(m)]
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i == m-1 and j == n-1:
                dp[i][j] = A[i][j]
            elif i == m-1:
                dp[i][j] = A[i][j]+dp[i][j+1]
            elif j == n-1:
                dp[i][j] = A[i][j]+dp[i+1][j]
            else:
                dp[i][j] = min(A[i][j]+dp[i+1][j],A[i][j]+dp[i][j+1])
    return dp[0][0]

print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))