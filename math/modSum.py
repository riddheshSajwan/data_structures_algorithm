'''
Problem Description

Given an array of integers A, calculate the sum of A [ i ] % A [ j ] for all possible i, j pairs. Return sum % (109 + 7) as an output.



Problem Constraints
1 <= length of the array A <= 105

1 <= A[i] <= 103



Input Format
The only argument given is the integer array A.



Output Format
Return a single integer denoting sum % (109 + 7).
'''

def solve(A):
    lst = [0] * 1009
    for a in A:
        lst[a] += 1
    ans = 0
    mod = 1000000007
    for i in range(1, 1001):
        if(lst[i] == 0):
            continue
        a = lst[i]
        for j in range(1, 1001):
            if(lst[j] == 0):
                continue
            b = lst[j]
            val = j % i
            temp = a * b * val
            ans = ((ans % mod) + (temp % mod)) % mod
    return ans

print(solve([17, 100, 11]))