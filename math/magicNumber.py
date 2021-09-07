'''
Problem Description

Given an integer A, find and return the Ath magic number.

A magic number is defined as a number which can be expressed as a power of 5 or sum of unique powers of 5.

First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….



Problem Constraints
1 <= A <= 5000



Input Format
The only argument given is integer A.



Output Format
Return the Ath magic number.
'''

def solve(A):
    
    magic_array = [0] + [0 for i in range(A)]
    i = 1
    exp = 1
    while i <= A:
        j = 1
        magic_array[i] = pow(5,exp)
        exp += 1
        while j < i and i < A:
            if i+j > A: break
            magic_array[i+j] = magic_array[i]+magic_array[j]
            j += 1
        i += j
    return magic_array[A]

def solve2(A):
    '''
    T = O(N), S = O(1)
    '''
    ans = 0
    x = 1
    while(A > 0):
        x *= 5
        if(A%2 == 1):
            ans += x
        A = A//2
    
    return ans
    

print(solve(10))
print(solve2(10))