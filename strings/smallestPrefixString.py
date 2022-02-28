'''
Problem Description
Given 2 strings A and B of size N and M respectively consisting of lowercase alphabets, find the lexicographically smallest string that can be formed by concatenating non empty prefixes of A and B (in that order).
Note: The answer string has to start with a non empty prefix of string A followed by a non empty prefix of string B.

Problem Constraints
1 <= N, M <= 100000

Input Format

First argument is a string A of size N.
Second argument is a string B of size M.

Output Format
Return a string denoting Lexicographically smallest string that can be formed by concatenating non empty prefixes of A and B (in that order).

Example Input
Input 1:
 A = "abba"
 B = "cdd"
Input 2:
 A = "acd"
 B = "bay"

Example Output
Output 1:
 "abbac"
Output 2:
 "ab"

Example Explanation
Explanation 1:
 We can concatenate prefix of A i.e "abba" and prefix of B i.e "c".
 The lexicographically smallest string will be "abbac".
Explanation 2:
 We can concatenate prefix of A i.e "a" and prefix of B i.e "b".
 The lexicographically smallest string will be "ab".
 '''

def smallestPrefix(A, B):
    res = A[0]
    i = 1
    while i < len(A) and ord(A[i]) < ord(B[0]):
        res += A[i]
        i += 1
    return res + B[0]

print(smallestPrefix("abba", "cdd"))