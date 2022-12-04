'''
https://leetcode.com/problems/unique-binary-search-trees/description/
'''

def numTrees(A) :
    dp = [0]*(A+1)
    dp[1] = 1
    dp[0] = 1
    '''def f(n):
        if dp[n] == -1:
            res = 0
            for i in range(n):
                #print(res)
                res += f(i)*f(n-i-1)
            dp[n] = res
        return dp[n]
    return f(A)'''
    for i in range(2,A+1):
        for j in range(i):
            dp[i] += dp[j]*dp[i-1-j]
    return dp[A]

print(numTrees(3))