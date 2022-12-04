'''
https://leetcode.com/problems/coin-change-ii/description/
'''

def change(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    
    for coin in coins:
        for i in range(coin, len(ways)):
            ways[i] += ways[i-coin]

    return ways[-1]

print(change(amount=5, coins=[1,2,5]))