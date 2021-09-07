'''
Problem Description

Given a positive integer A. Return an array of minimum length whose elements represent the powers of 3 and the sum of all the elements is equal to A.



Problem Constraints
1 <= A <= 109



Input Format
Single argument is an integer A.



Output Format
Return an array of minimum length of powers of 3 whose elements sums to A.
'''

def solve(A):
    res,fin_res = [],[]
    while A > 0:
        res.append(A%3)
        A //= 3
    for i in range(len(res)):
        while res[i] > 0:
            fin_res.append(pow(3,i))
            res[i] -= 1
    return fin_res

print(solve(13))