'''
Problem Description

Given two integers A and B. Find the value of A-1 mod B where B is a prime number and gcd(A, B) = 1.

A-1 mod B is also known as modular multiplicative inverse of A under modulo B.



Problem Constraints
1 <= A <= 109
1<= B <= 109
B is a prime number



Input Format
First argument is an integer A.
Second argument is an integer B.



Output Format
Return an integer denoting the modulor inverse
'''
def solve(A, B):
    '''
    X = A^(-1)modB
    X*A = 1modB
    
    Fermats’s little theorem:

    A^(B-1) ≡ 1 (mod B) where B is prime and A is not a multiple of B.
    Multiply by A-1 on both sides, We get
    
    A^(B-2) ≡ A-1 (mod B) where B is prime and A is not a multiple of B.
    '''

    return pow(A,B-2,B)

print(solve(6, 23))