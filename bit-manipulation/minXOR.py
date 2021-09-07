'''
Problem Description

Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.



Problem Constraints
2 <= length of the array <= 100000
0 <= A[i] <= 109



Input Format
First and only argument of input contains an integer array A.



Output Format
Return a single integer denoting minimum xor value.
'''

def findMinXor(A):
    A.sort()
    res = float('inf')
    for i in range(1,len(A)):
        res = min(res,A[i-1]^A[i])
    return res

print(findMinXor([0, 2, 5, 7]))