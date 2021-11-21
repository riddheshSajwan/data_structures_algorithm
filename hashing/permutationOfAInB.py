'''
Problem Description

You are given two strings A and B of size N and M respectively.
You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.

Problem Constraints
1 <= N < M <= 105

Input Format
Given two argument, A and B of type String.

Output Format
Return a single Integer, i.e number of permutations of A present in B as a substring.

Example Input
Input 1:
 A = "abc"
 B = "abcbacabc"
Input 2:
 A = "aca"
 B = "acaa"

Example Outpu
Output 1:
 5
Output 2:
 2

Example Explanation
Explanation 1:
 Permutations of A that are present in B as substring are:
    1. abc
    2. cba
    3. bac
    4. cab
    5. abc
    So ans is 5.
Explanation 2:
 Permutations of A that are present in B as substring are:
    1. aca
    2. caa 
'''

def solve(A, B):
    res = 0
    freq_arr = [0 for i in range(26)]
    slide_freq = [0 for i in range(26)]
    for item in A:
        freq_arr[ord(item)%26] += 1
    i,j = 0,len(A)-1
    for k in range(i,j+1):
        slide_freq[ord(B[k])%26] += 1
    while True:
        res += 1
        for k in range(26):
            if freq_arr[k] != slide_freq[k]:
                res -= 1
                break
        slide_freq[ord(B[i])%26] -= 1
        i += 1
        j += 1
        if j < len(B):
            slide_freq[ord(B[j])%26] += 1
        else: 
            return res

A = "abc"
B = "abcbacabc"
print(solve(A, B))