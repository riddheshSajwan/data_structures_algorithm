'''
Problem Description

Given an array of integers A and an integer B, find and return the number of pairs in A whose sum is divisible by B.

Since the answer may be large, return the answer modulo (109 + 7).



Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 106



Input Format
The first argument given is the integer array A.
The second argument given is the integer B.



Output Format
Return the total number of pairs for which the sum is divisible by B modulo (109 + 7).
'''

def solve(A, B):
    B %= int(1e9+7)
    mod_array = [0 for i in range(B)]
    for item in A:
        mod_array[item%B] += 1
    ans = 0
    for i in range(B//2 + 1):
        if i == 0 or (B%2 == 0 and i == B//2):
            ans += mod_array[i]*(mod_array[i]-1)//2
        else:
            ans += mod_array[i]*mod_array[B-i]
    return ans%int(1e9+7)

print(solve([5, 17, 100, 11], 28))