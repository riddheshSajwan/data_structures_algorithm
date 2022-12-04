'''
https://leetcode.com/problems/interleaving-string/description/
'''

def isInterleave(A: str, B: str, C: str) -> bool:
    a = len(A)
    b = len(B)
    c = len(C)
    if c != a+b:
        return 0
    dp = [[[0]*(c+1) for j in range(b+1)] for i in range(a+1)]
    # def f(i,j,idx):
    #     #base-case
    #     if idx == c:
    #         return 1
    #     if i == a:
    #         #print(i,j,idx)
    #         return int(B[j:] == C[idx:])
    #     if j == b:
    #         #print(i,j,idx,A[i:],C[idx:])
    #         return int(A[i:] == C[idx:])
    #     if A[i] == C[idx] and B[j] == C[idx]:
    #         return f(i+1,j,idx+1) or f(i,j+1,idx+1)
    #     elif A[i] == C[idx]:
    #         return f(i+1,j,idx+1)
    #     elif B[j] == C[idx]:
    #         return f(i,j+1,idx+1)
    #     #print(A[i],B[j],C[idx])
    #     return 0
    # return f(0,0,0)
    for i in range(a,-1,-1):
        for j in range(b,-1,-1):
            for idx in range(c,-1,-1):
                if idx == c:
                    dp[i][j][idx] = 1
                elif i == a:
                    dp[i][j][idx] = int(B[j:] == C[idx:])
                elif j == b:
                    dp[i][j][idx] = int(A[i:] == C[idx:])
                elif A[i] == C[idx] and B[j] == C[idx]:
                    dp[i][j][idx] = dp[i+1][j][idx+1] or dp[i][j+1][idx+1]
                elif A[i] == C[idx]:
                    dp[i][j][idx] = dp[i+1][j][idx+1]
                elif B[j] == C[idx]:
                    dp[i][j][idx] = dp[i][j+1][idx+1]
                else:
                    dp[i][j][idx] = 0
    return dp[0][0][0]

print(isInterleave(A = "aabcc", B = "dbbca", C = "aadbbcbcac"))