'''
https://leetcode.com/problems/longest-common-prefix/
'''
def longestCommonPrefix(A):
    res = A[0]
    for i in range(1,len(A)):
        idx = 0
        for j in range(min(len(A[i]),len(res))):
            if res[idx] == A[i][j]:
                idx += 1
                continue
            break
        res = res[:idx]
    return res

print(longestCommonPrefix(["flower","flow","flight"]))