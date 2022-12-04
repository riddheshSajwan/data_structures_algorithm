'''
https://leetcode.com/problems/distinct-subsequences/description/
'''

def numDistinct(A, B):
    n = len(A)
    m = len(B)
    '''def solve(i,j,size):
        if i == n or j == m:
            return int(size == m)
        if A[i] == B[j]:
            take = solve(i+1,j+1,size+1)
            not_take = solve(i+1,j,size)
            return take + not_take
        return solve(i+1,j,size)
    return solve(0,0,0)'''
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(n,-1,-1):
        for j in range(m,-1,-1):
            if i == n and j == m:
                dp[i][j] = 1
            elif i == n or j == m:
                dp[i][j] = 1 if j == m else 0
            elif A[i] == B[j]:
                dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
            else:
                dp[i][j] = dp[i+1][j]
    return dp[0][0]

print(numDistinct("babgbag", "bag"))