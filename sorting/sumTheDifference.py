'''
Given an integer array A of size N.
You have to find all possible non-empty subsequence of the array of numbers and then, for each subsequence, find the difference between the largest and smallest numbers in that subsequence Then add up all the differences to get the number.

As the number may be large, output the number modulo 1e9 + 7 (1000000007).

NOTE: Subsequence can be non-contiguous.
Example Input
Input 1:

A = [1, 2]
Input 2:

A = [1]
Example Explanation
Explanation 1:

All possible non-empty subsets are:
[1]    largest-smallest = 1 - 1 = 0
[2]    largest-smallest = 2 - 2 = 0
[1 2]  largest-smallest = 2 - 1 = 1
Sum of the differences = 0 + 0 + 1 = 1
So, the resultant number is 1
Explanation 2:

 Only 1 subsequence of 1 element is formed.
'''
def solve(A):
    '''
    {A[N-1]2^(N-1) +A[N-2]2^(N-2) +…..+A[0]2^0} - {A[0]2^(N-1) + A[1]2^(N-2) +……+ A[0]2^0}
    for any i (0->N-1), we are finding the number of occurrences when A[i] will be min and when it will be max in all the subsequences.
    '''
    MOD = int(1e9+7)
    n = len(A)
    A.sort()
    X = Y = 0
    for i in range(n):
        X += A[i] * pow(2,n-1-i,MOD) 
    for i in range(n-1,-1,-1):
        Y += A[i] * pow(2,i,MOD)
    return (Y-X)%MOD

print(solve([1,2]))