'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
# Dynamic Programming solution - a bit slower and comes with O(n) space complexity.
def maxProfitDP(prices):
  size = len(prices)
  if size == 0: return 0
  profit = []
  minBuy = 0
  for i in range(size):
    if i == 0:
      minBuy = prices[0]
      profit.append(0)
    else:
      minBuy = min(minBuy,prices[i-1])
      profit.append(max(prices[i]-minBuy, profit[i-1]))
                              
  return profit[size-1]

print(maxProfitDP([7,1,5,3,6,4]))

# Normal array solution with O(1) space complexity.
def maxProfit(prices):
  buy = prices[0]
  maxProfit = 0
  
  for price in prices:
    if price < buy:
      buy = price
    else:
      maxProfit = max(maxProfit,price - buy)
  
  return maxProfit

print(maxProfit([7,1,5,3,6,4]))