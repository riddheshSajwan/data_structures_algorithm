'''
https://leetcode.com/problems/climbing-stairs/
'''

# Time O(n) Space O(n)
def climbStairs(n): 
    if n == 0: return 0
    ways = []
    
    for stairs in range(1,n+1):
        i = stairs - 1
        if stairs == 1: ways.append(1)
        elif stairs == 2: ways.append(2)
        else: ways.append(ways[i-1] + ways[i-2])
    
    return ways[n-1]

print(climbStairs(9))

# Time O(n) Space O(n)
def climbStairsRecursive(n):
    if n == 0: return 0
    waysCache = {}
      
    def _climbStairs(n):
        if n == 1: return 1
        elif n == 2: return 2
        else: 
            if waysCache.get(n): return waysCache[n]
            else: 
                waysCache.update({n:_climbStairs(n-1) + _climbStairs(n-2)})
                return waysCache[n]
      
    return _climbStairs(n)

print(climbStairsRecursive(39))

# Both perform same.