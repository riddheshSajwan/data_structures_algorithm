'''
https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1
'''

def knapSack(n, A, B, C):
    # code here
    dp = [0 for i in range(A+1)]
    for cap in range(A+1):
        for i in range(n):
            if cap - C[i] >= 0:
                dp[cap] = max(dp[cap],B[i]+dp[cap-C[i]])
    return dp[A]

print(knapSack(2, 3, [1,1], [2,1]))