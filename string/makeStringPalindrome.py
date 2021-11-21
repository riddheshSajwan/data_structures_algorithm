'''
Problem Description
Given a string A of size N consisting only of lowercase alphabets. The only operation allowed is to insert characters in the beginning of the string.
Find and return how many minimum characters are needed to be inserted to make the string a palindrome string.

Problem Constraints
1 <= N <= 106

Input Format
The only argument given is a string A.

Output Format
Return an integer denoting the minimum characters that are needed to be inserted to make the string a palindrome string.

Example Input
Input 1:
 A = "abc"
Input 2:
 A = "bb"

Example Output
Output 1:
 2
Output 2:
 0

Example Explanation
Explanation 1:
 Insert 'b' at beginning, string becomes: "babc".
 Insert 'c' at beginning, string becomes: "cbabc".
Explanation 2:
 There is no need to insert any character at the beginning as the string is already a palindrome. 
 '''

class Solution:
	# @param A : string
	# @return an integer
    def getZarr(self, string, z, n):
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
        return z
    def getPeriod(self,z,n):
        for i in range(1,n):
            if z[i] + i == n:
                return i
        return n
    def solve(self, A):
        n = len(A)
        new_A = A + A[::-1] # string + reverse(string)
        z = [0 for i in range(2*n)]
        z = self.getZarr(new_A,z,2*n)
        #print(z)
        period = self.getPeriod(z,2*n)
        #print(period)
        return n - (2*n%period) if period != 1 else 0 # (2*n - period) will give the length of common suffix and prefix

        # to make a palindrome, find the length of the longest common prefix which is also a suffix in string + reverse(string), and substract the length of this suffix/prefix from length of initial string.

print(Solution().solve("bbab"))
