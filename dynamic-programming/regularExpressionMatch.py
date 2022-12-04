'''
https://www.interviewbit.com/problems/regular-expression-match/
'''

def isMatch(A, B):
    n = len(A)
    m = len(B)
    dp = [[False]*(m+1) for i in range(n+1)]
    for i in range(n,-1,-1):
        for j in range(m,-1,-1):
            #print(i,j)
            if i == n and j == m:
                dp[i][j] = True
            elif i == n:
                if B[j] == '*':
                    dp[i][j] = True and dp[i][j+1]
            elif j == m:
                continue
            else:
                if A[i] == B[j] or B[j] == "?":
                    #print("enter",dp[i+1][j+1])
                    dp[i][j] = True and dp[i+1][j+1]
                elif B[j] == "*":
                    dp[i][j] = (True and dp[i+1][j]) or dp[i][j+1]
    #print(dp)
    return int(dp[0][0])

print(isMatch("aab", "c*a*b"))