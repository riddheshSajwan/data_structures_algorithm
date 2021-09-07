'''
Problem Description

You have an array A with N elements. We have 2 types of operation available on this array :
We can split a element B into 2 elements C and D such that B = C + D.
We can merge 2 elements P and Q as one element R such that R = P^Q i.e XOR of P and Q.
You have to determine whether it is possible to make array A containing only 1 element i.e. 0 after several splits and/or merge?

Problem Constraints
1 <= N <= 100000

1 <= A[i] <= 106


Input Format
The first argument is an integer array A of size N.

Output Format
Return "Yes" if it is possible otherwise return "No".
'''
def solve(A):
    odd_count = 0
    for item in A:
        odd_count += item%2
    if odd_count%2 == 0: return "Yes" 
    else: return "No"

print(solve([9, 17]))
        
