'''
https://leetcode.com/problems/longest-common-subsequence/description/
'''

def longestCommonSubsequence(A, B):
    n = len(A)
    m = len(B)
    prev = [0]*(m+1)
    curr = [0]*(m+1)
    #print(dp)
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if A[i] == B[j]:
                curr[j] = 1 + prev[j+1]
            else:
                curr[j] = max(curr[j+1], prev[j])
        for j in range(m+1):
            prev[j] = curr[j]
    return curr[0]

print(longestCommonSubsequence("abc", "ace"))