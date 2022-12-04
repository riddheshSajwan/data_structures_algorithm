'''
https://leetcode.com/problems/longest-palindromic-subsequence/description/
'''

def longestPalindromeSubseq(A):
    n = len(A)
    dp = [[-1]*(n) for j in range(n)]
    def foo(i,j):
        if i == j:
            return 1
        if i > j:
            return 0
        if dp[i][j] == -1:
            if A[i] == A[j]:
                dp[i][j] = 2 + foo(i+1,j-1)
            else:
                dp[i][j] = max(foo(i+1,j),foo(i,j-1))
        return dp[i][j]
    return foo(0,n-1)

print(longestPalindromeSubseq("bbbab"))