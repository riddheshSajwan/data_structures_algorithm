'''
Problem Description

Given an integer A.
Two numbers X and Y are defined as follows:

X is the greatest number smaller than A such that XOR sum of X and A is the same as the sum of X and A.
Y is the smallest number greater than A such that XOR sum of Y and A is the same as the sum of Y and A.
Find and return the XOR of X and Y.

NOTE 1: XOR of X and Y is defined as X ^ Y where '^' is the BITWISE XOR operator.

NOTE 2: Your code will be run against a maximum of 100000 Test Cases.



Problem Constraints
1 <= A <= 109



Input Format
First and only argument is an integer A.



Output Format
Return an integer denoting the XOR of X and Y.
'''

def solve(A):
    temp = A
    exp = 0
    while A > 0:
        A >>= 1
        exp += 1
    return pow(2,exp)^(pow(2,exp)-temp-1)

print(solve(37))