'''
Problem Description

Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.

Find the maximum value of GCD.



Problem Constraints
2 <= N <= 105
1 <= A[i] <= 109



Input Format
First argument is an integer array A.



Output Format
Return an integer denoting the maximum value of GCD.
'''

def solve(A):
    n = len(A)
    max_gcd = float('-inf')
    prefix_gcd, suffix_gcd = [0 for i in range(len(A))], [0 for i in range(len(A))]
    prefix_gcd[0], suffix_gcd[-1] = A[0], A[-1]
    def gcd(a,b):
        if b == 0:
            return a
        return gcd(b,a%b)
    for i in range(1,n):
        prefix_gcd[i],suffix_gcd[n-1-i] = gcd(A[i],prefix_gcd[i-1]), gcd(A[n-1-i],suffix_gcd[n-i])
    
    for i in range(n):
        if i ==0:
            max_gcd = max(max_gcd,suffix_gcd[i+1])
        elif i == n-1:
            max_gcd = max(max_gcd,prefix_gcd[i-1])
        else:
            max_gcd = max(max_gcd,gcd(prefix_gcd[i-1],suffix_gcd[i+1]))
    return max_gcd
        
print(solve([12, 15, 18]))