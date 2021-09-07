'''
Problem Description

Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Note: Output array must be sorted.

Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 109

Input Format
First argument is an array of interger of size N.

Output Format
Return an array of two integers that appear only once.
'''

def solve(A):
    all_xor = 0
    for item in A:
        all_xor ^= item
    bit = 1
    while all_xor&bit != bit:
        bit <<= 1
    res = [0,0]
    for item in A:
        if item&bit == all_xor&bit:
            res[0] ^= item
        else:
            res[1] ^= item
    res.sort()
    return res

print(solve([1, 2, 3, 1, 2, 4]))