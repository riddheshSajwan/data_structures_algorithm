'''
https://leetcode.com/problems/coin-change/
'''
#recursive top-down solution
def coinChange(coins,amount):
    cache = [-1]*(amount+1)
    cache[0] = 0
    
    def _coinChange(rem_amount):
        if cache[rem_amount] == -1:
            cache[rem_amount] = float('inf')
            for coin in coins:
                temp = rem_amount - coin
                if temp >=0:
                    cache[rem_amount] = min(1+_coinChange(temp),cache[rem_amount])
        return cache[rem_amount]
    
    result = _coinChange(amount)
    return result if result != float('inf') else -1

print(coinChange([186,419,83,408], 6249))

#iterative bottom-up approach. very effecient.
def coinChange2(coins,amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1

print(coinChange2([186,419,83,408], 6249))