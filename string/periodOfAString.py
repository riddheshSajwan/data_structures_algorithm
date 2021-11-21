'''
Problem Description
Given a string A of length N consisting of lowercase alphabets. Find the period of the string.
Period of the string is the minimum value of k (k >= 1), that satisfies A[i] = A[i % k] for all valid i.

Problem Constraints
1 <= N <= 106

Input Format
First and only argument is a string A of length N.

Output Format
Return an integer, denoting the period of the string.

Example Input
Input 1:
 A = "abababab"
Input 2:
 A = "aaaa"

Example Output
Output 1:
 2
Output 2:
 1

Example Explanation
Explanation 1:
 Period of the string will be 2: 
 Since, for all i, A[i] = A[i%2]. 
Explanation 2:
 Period of the string will be 1.
 '''
def solve(A):
    n = len(A)
    z = [0 for i in range(n)]
    z[0] = n
    def getZarr(string, z):
        l, r, k = 0, 0, 0
        for i in range(1, n):
            if i > r:
                l, r = i, i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1
            else:
                k = i - l
                if z[k] < r - i + 1:
                    z[i] = z[k]
                else:
                    l = i
                    while r < n and string[r - l] == string[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1
    getZarr(A,z)
    for i in range(1,n):
        if z[i] + i == n:
            return i
    return n

print(solve("abababab"))