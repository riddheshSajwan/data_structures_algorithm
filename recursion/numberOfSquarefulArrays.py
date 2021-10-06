'''
https://leetcode.com/problems/number-of-squareful-arrays/
'''

# find a map of all perfect square pairs = square_map
# create a freq_map
# find out the total number of paths possible to create arrays of len = n using dfs in square_map
# divide the toal number of factorials of repeating numbers
# TC = O(n^2) SC = O(n)
def solve(A):
    n = len(A)
    if n == 1:
        return 0
    def isPerfectSquare(num):
        sqroot = pow(num,0.5)
        return sqroot - int(sqroot) == 0
    square_map = {i:[] for i in range(n)}
    freq_map = {}
    for i in range(n):
        if A[i] in freq_map: freq_map[A[i]] += 1
        else: freq_map[A[i]] = 1
        for j in range(i+1,n):
            if isPerfectSquare(A[i]+A[j]):
                square_map[i].append(j)
                square_map[j].append(i)
    def _dfs(visited,node):
        #print(visited,node)
        if len(visited) == n:
            return 1
        _count = 0
        for adj in square_map[node]:
            if adj not in visited:
                visited.add(adj)
                _count += _dfs(visited,adj)
                visited.remove(adj)
        #print(visited,node,_count)
        return _count
    visited = set()
    count = 0
    for node in square_map:
        visited.add(node)
        count += _dfs(visited,node)
        visited.remove(node)
    fact_arr = [1 for i in range(n+1)]
    for i in range(1,n+1):
        fact_arr[i] = fact_arr[i-1]*i
    divisor = 1
    for key in freq_map:
        divisor *= fact_arr[freq_map[key]]
    return count//divisor

print(solve([1,17,8]))

import collections
# Best Solution
def numSquarefulPerms(A):
    N = len(A)
    if N == 1:
        return 0
    count = collections.Counter(A)
    graph = {x: [] for x in count}
    for x in count:
        for y in count:
            if int((x+y)**.5 + 0.5) ** 2 == x + y:
                graph[x].append(y)
    def dfs(x, todo):
        count[x] -= 1
        if todo == 0:
            ans = 1
        else:
            ans = 0
            for y in graph[x]:
                if count[y]:
                    ans += dfs(y, todo - 1)
        count[x] += 1
        return ans
    return sum(dfs(x, len(A) - 1) for x in count)
print(numSquarefulPerms([1,17,8]))