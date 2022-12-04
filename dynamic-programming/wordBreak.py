"""
https://leetcode.com/problems/word-break/description/
"""

def wordBreak(A, B):
    segments = set()
    b = len(B)
    a =len(A)
    dp = [0]*(a+1)
    segments = set(B)
    '''def f(beg):
        if dp[beg] == 0:
            if A[beg:] in segments:
                dp[beg] = 1
            else:
                for end in range(beg+1,a+1):
                    if A[beg:end] in segments:
                        dp[beg] = 1&f(end)
                    if dp[i] == 1:
                        break
        return dp[beg]
    res = f(0)
    return 0 if res <=0 else 1'''
    for i in range(a,-1,-1):
        if A[i:] in segments:
            dp[i] = 1
        else:
            for j in range(i+1,a+1):
                if A[i:j] in segments:
                    dp[i] = 1&dp[j]
                if dp[i] == 1:
                    break
    return dp[0]

print(wordBreak("leetcode", ["leet","code"]))