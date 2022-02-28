'''
https://leetcode.com/problems/k-diff-pairs-in-an-array/
https://practice.geeksforgeeks.org/problems/find-pair-given-difference1559/1#
'''

def solve(A, B):
    '''
    2 pointer
    i,j = 0,1
    n = len(A)
    res = 0
    unique_A = set(A)
    while j < n:
        if A[j]-A[i] == B:
            res += 1
            while j < n and A[j+1] == A[j]:
                j += 1
            while i < n and A
    '''
    # hashset approach
    cache = set()
    res = 0
    if B == 0:
        freq_map = {}
        for item in A:
            if item not in freq_map:
                freq_map[item] = 0
            freq_map[item] += 1
        for key in freq_map:
            if freq_map[key] > 1: res += 1
        return res
    unique_A = set(A)
    if len(unique_A) == 1:
        unique_A = [A[0],A[1]]
    for item in unique_A:
        #print(item)
        if item in cache:
            res += 1
        if item >= B:
            cache.add(item-B)
        cache.add(B+item)
        #print(cache,res)
    return res

print(solve([8, 12, 16, 4, 0, 20], 4))