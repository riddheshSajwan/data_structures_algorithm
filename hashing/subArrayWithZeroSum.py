'''
https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1
'''

def solve(arr):
    n = len(arr)
    n_sum = 0
    s = set()
    
    for i in range(n):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in s:
            return 1
        s.add(n_sum)
    
    return 0

print(solve([1, 2, 3, 4, 5]))