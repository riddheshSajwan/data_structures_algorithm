def knapSack(W, wt, val, n):
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

print(knapSack(4, [4,5,1], [1,2,3], 3))