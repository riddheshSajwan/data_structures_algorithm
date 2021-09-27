'''
Given an array of integers A of size N where N is even.

Divide the array into two subsets such that

1.Length of both subset is equal.
2.Each element of A occurs in exactly one of these subset.
Magic number = sum of absolute difference of corresponding elements of subset.

Note: You can reorder the position of elements within the subset to find the value of magic number.

For Ex:- 
subset 1 = {1, 5, 1}, 
subset 2 = {1, 7, 11}
Magic number = abs(1 - 1) + abs(5 - 7) + abs(1 - 11) = 12
Return an array B of size 2, where B[0] = maximum possible value of Magic number modulo 109 + 7, B[1] = minimum possible value of a Magic number modulo 109 + 7.
'''
'''
Initially sort the array.
For the minimum magic, find the sum of difference between adjacent elements in pairs of two.
For the maximum magic, find the sum of difference between the two elements equidistant from the front and back of the array.
'''

def solve(A):
    MOD = int(1e9+7)
    A.sort()
    min_sum,max_sum = 0,0
    n = len(A)
    for i in range(n-1):
        min_sum += A[i+1]-A[i] if i%2 == 0 else 0
        max_sum += A[n-i-1]-A[i] if i < n//2 else 0
    return [max_sum%MOD,min_sum%MOD]
print(solve([3, 11, -1, 5]))
