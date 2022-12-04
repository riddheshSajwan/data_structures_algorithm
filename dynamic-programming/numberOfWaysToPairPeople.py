'''
https://www.geeksforgeeks.org/number-of-ways-to-pair-people/
'''

def solve(A):
    MOD = 10003
    dp = [0 for i in range(A+1)]
    dp[0],dp[1] = 1,1
    for i in range(2,A+1):
        dp[i] = dp[i-1]%MOD + (i-1)%MOD*dp[i-2]%MOD
    return dp[A]%MOD

print(solve(5))