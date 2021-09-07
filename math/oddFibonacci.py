'''
Problem Description

Given two integers A and B representing an interval [A, B].

Fibonacci sequence is a sequence whose definition is as follows:

F[1] = 1 , F[2] = 1

F[i] = F[i-1] + F[i-2] for i > 2

Your task is to find the count of integers x in the range [A, B] such that F[x] is odd.

Problem Constraints
1 <= A <= 109
1 <= B <= 109
A <= B

Input Format
The first argument given is an integer A.

The second argument given is an integer B.

Output Format
Return the count of integers x in the range [A, B] such that F[x] is odd.
'''

def solve(A, B):
    '''Try to write some fibonacci numbers you will find the pattern.

        The pattern is that:
        
        For every multiple of 3 it’s fibonacci is even.
        
        Like: F[3]=2, F[6]=8, F[9]=34
        
        So Just find the count of multiples of 3 between A and B and subtract it from total numbers between A and B.
        
        Total Numbers Between A and B = B - A +1
        
        Count of Multiples of 3 between A and B = (B/3) - ((A-1)/3)
        
        So answer will be = (B-A+1) - ((B/3)-((A-1)/3))

    '''
    return (B-A+1) - ((B//3)-((A-1)//3))

print(solve(6, 20))