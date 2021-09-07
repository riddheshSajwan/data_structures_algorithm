'''
Problem Description

Scooby has 3 three integers A, B and C.

Scooby calls a positive integer special if it is divisible by B and it is divisible by C. You need to tell number of special integers less than or equal to A.

Problem Constraints
1 <= A, B, C <= 109

Input Format
First argument is a positive integer A
Second argument is a positive integer B
Third argument is a positive integer C

Output Format
One integer corresponding to the number of special integers less than or equal to A.
'''

def solve(A, B, C):
    def gcd(a,b):
        if b == 0:
            return a
        return gcd(b,a%b)
    lcm = (B*C)//gcd(B,C)
    return A//lcm

print(solve(12, 3, 2))