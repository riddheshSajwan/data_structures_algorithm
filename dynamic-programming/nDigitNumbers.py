'''
https://www.interviewbit.com/problems/n-digit-numbers-with-digit-sum-s-/
'''

def solve(A, B):
    MOD = int(1e9+7)
    dp = [[0]*(B+1) for i in range(A+1)]
    '''def count(D,S):
        if S == 0:
            return 1
        if S < 0 or D == 0:
            return 0
        if dp[D][S] == -1:
            dp[D][S] = 0
            if D != A:
                dp[D][S] += count(D-1,S-0)
            for digit in range(1,10):
                dp[D][S] += count(D-1,S-digit)
        
        return dp[D][S]'''
    for D in range(1,A+1):
        for S in range(B+1):
            if D != A:
                dp[D][S] += dp[D-1][S-0]%MOD
            for digit in range(1,10):
                if S - digit == 0:
                    dp[D][S] += 1
                elif S-digit >= 0 and S <= 9*D:
                    dp[D][S] += dp[D-1][S-digit]%MOD
    #print(dp)
    return dp[A][B]%MOD

print(solve(2, 4))