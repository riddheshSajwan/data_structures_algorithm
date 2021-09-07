''''
Problem Description

Given an array of integers A, every element appears twice except for one. Find that single one.

NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


Problem Constraints
2 <= |A| <= 2000000

0 <= A[i] <= INTMAX

Input Format
First and only argument of input contains an integer array A


Output Format
Return a single integer denoting the single element.'''

def singleNumber(A):
    res = 0
    for item in A:
        res ^= item
    return res

print(singleNumber([1, 2, 2, 3, 1]))