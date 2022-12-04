'''
https://www.interviewbit.com/problems/intersecting-chords-in-a-circle/
'''

def chordCnt(A):
    MOD = int(1e9+7)
    dp = [0]*(A+1)
    dp[0] = dp[1] = 1
    for i in range(2,A+1):
        for j in range(i):
            #print(j,i-j-1)
            dp[i] += dp[j]*dp[i-j-1]
            dp[i] %= MOD
    return dp[A]

print(chordCnt(2))