'''
https://leetcode.com/problems/consecutive-numbers-sum/
'''

def solve(A):
    while((A & 1) == 0):
        A = A // 2
    ans = 1
    d = 3
    while(d * d <= A):
        e = 0
        while(A % d == 0):
            A = A // d
            e += 1
        ans *= e + 1
        d += 2
    if(A > 1):
        ans = ans * 2
    return ans

print(solve(15))