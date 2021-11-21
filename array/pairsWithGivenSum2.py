'''
https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1#
'''
def solve(A, B):
    cache = {}
    res = 0
    for item in A:
        if item in cache:
            res += cache[item]
        if B-item not in cache:
            cache[B-item] = 0
        cache[B-item] += 1
    return res%(int(1e9+7))

print(solve([1, 1, 1], 2))