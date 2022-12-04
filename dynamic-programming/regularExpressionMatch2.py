'''
https://leetcode.com/problems/regular-expression-matching/description/
'''

def isMatch(A, B):
    n = len(A)
    m = len(B)
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(n,-1,-1):
        for j in range(m,-1,-1):
            if i == n and j == m:
                dp[i][j] = 1
            elif i == n:
                if (B[j] == "*") or (j < m-1 and B[j+1] == "*"):
                    dp[i][j] = dp[i][j+1]
            elif j == m:
                continue
            else:
                if B[j] == A[i] or B[j] == ".":
                    if j < m-1 and B[j+1] == "*":
                        dp[i][j] = dp[i][j+2] | dp[i+1][j]
                    else:
                        dp[i][j] = dp[i+1][j+1]
                elif B[j] == "*":
                    dp[i][j] = dp[i+1][j] | dp[i][j+1]
                elif j < m-1 and B[j+1] == "*":
                    dp[i][j] = dp[i][j+2]
    #print(dp)
    return dp[0][0] 

print(isMatch("ab", ".*"))