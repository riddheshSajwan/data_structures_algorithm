'''
https://practice.geeksforgeeks.org/problems/get-minimum-squares0538/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
'''

def MinSquares(A):
    # Code here
    dp = [1 for i in range(A+1)]
    dp[0] = 0
    dp[1] = 1
    sqrs = [x * x for x in range(1,330)]
    for i in range(2,A+1):
        j = 1
        res = float('inf')
        for x in sqrs:
            if x > i: break
            res = min(res,1+dp[i-x])
        dp[i] = res
        #print(dp)
    return dp[A]

print(MinSquares(6))