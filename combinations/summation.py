'''
Problem Description

Given an integer A.

Calculate the sum = (ACr) * (r) * (r - 1) * (2r-2) for all r from 0 to A.

Return sum % 109 + 7.
'''

def solve(A):
    '''
    (1+x)A = 1 + AC1 x + AC2 x2 + AC3 x3 + …. + xA

    Differentiating w.r.t x both sides we get:

    A(1+x)(A-1) = AC1 + 2AC2 x + 3AC3 x2 +…. + AxA-1

    Differentiating w.r.t x again both sides we get:

    A(A-1)(1+x)A-2 = 2AC2 + 6 AC3 x + …. + A(A-1)xA-2

    Putting x=2 we get:

    A(A-1)3A-2 = 2AC2 + 12AC3+…. + A(A-1)3A-2

    So the right term is what we have to find so just calculate:

    A(A-1)3A-2 using modulo exponentiation and multiplication.
    '''
    MOD = int(1e9+7)
    return A*(A-1)*(pow(3,A-2,MOD))%MOD

print(solve(5))