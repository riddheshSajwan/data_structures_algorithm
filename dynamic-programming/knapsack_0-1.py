'''
https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
'''
def knapSack(C, B, A, n):
       
        # code here
        dp = [[0]*(C+1) for i in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(C,-1,-1):
                if j - B[i] >= 0:
                    dp[i][j] = max(A[i]+dp[i+1][j-B[i]],dp[i+1][j])
                else:
                    dp[i][j] = dp[i+1][j]
        #print(dp)
        return dp[0][C]

print(knapSack(4, [4,5,1], [1,2,3], 3))

def knapSack2(W, wt, val, n):
    if n == 0 or wt == [] or val == []:
        return 0
    
    dp = [[-1 for i in range(n)] for i in range(W)]
    
    def _knapSack(W,wt,val,n):
        if W == 0 or n == 0:
            return 0
        if W - wt[n-1] >= 0:
            if dp[W-wt[n-1]][n-1] == -1:
                dp[W-wt[n-1]][n-1] = max(val[n-1] + _knapSack(W-wt[n-1],wt[:n-1],val[:n-1],n-1), _knapSack(W,wt[:n-1],val[:n-1],n-1))
            return dp[W-wt[n-1]][n-1]
        return _knapSack(W,wt[:n-1],val[:n-1],n-1)
    return _knapSack(W,wt,val,n)

print(knapSack2(4, [4,5,1], [1,2,3], 3))