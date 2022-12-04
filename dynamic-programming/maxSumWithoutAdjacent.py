'''
https://www.interviewbit.com/problems/max-sum-without-adjacent-elements/
'''

def adjacent(A):
    n = len(A[0])
    new_A = [0]*n
    for i in range(n):
        new_A[i] = max(A[0][i],A[1][i])
    dp = [0]*(n+2)
    for i in range(n-1,-1,-1):
        dp[i] = max(new_A[i] + dp[i+2], dp[i+1])
    return dp[0]

A = [   [1, 2, 3, 4],
            [2, 3, 4, 5]    ]
print(adjacent(A))