'''
Problem Description

There are N players each with strength A[i]. when player i attack player j, player j strength reduces to max(0, A[j]-A[i]). When a player's strength reaches zero, it loses the game and the game continues in the same manner among other players until only 1 survivor remains.

Can you tell the minimum health last surviving person can have?

Problem Constraints
1 <= N <= 100000

1 <= A[i] <= 1000000

Input Format
First and only argument of input contains a single integer array A.

Output Format
Return a single integer denoting minimum health of last person.
'''

def solve(A):
    def gcd(a,b):
        if b == 0 :
            return a
        return gcd(b%a,a)
    rolling_gcd = A[0]
    for item in A[1:]:
        rolling_gcd = gcd(rolling_gcd,item)
    return rolling_gcd

print(solve([2, 3, 4]))