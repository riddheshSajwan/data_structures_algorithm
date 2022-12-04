'''
https://leetcode.com/problems/dungeon-game/description/
'''

def calculateMinimumHP(A):
    n = len(A)
    m = len(A[0])
    dp = [[float('inf')]*(m+1) for i in range(n+1)]
    dp[n][m-1] = dp[n-1][m] = 1
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            temp = min(dp[i][j+1], dp[i+1][j])
            if A[i][j] < temp:
                dp[i][j] = temp - A[i][j]
            else:
                dp[i][j] = 1
            #need = min(dp[i][j+1], dp[i+1][j]) - A[i][j]
            #dp[i][j] = max(need,1)
    #print(dp)
    return dp[0][0]

print(calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))