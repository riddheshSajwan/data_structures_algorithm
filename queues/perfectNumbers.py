'''
Problem Description
Given an integer A, you have to find the Ath Perfect Number.
A Perfect Number has the following properties:
It comprises only 1 and 2.
The number of digits in a Perfect number is even.
It is a palindrome number.
For example 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.

Problem Constraints
1 <= A <= 100000

Input Format
The only argument given is an integer A.

Output Format
Return a string that denotes the Ath Perfect Number.

Example Input
Input 1:
 A = 2
Input 2:
 A = 3

Example Output
Output 1:
 22
Output 2:
 1111

Example Explanation
Explanation 1:
First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221
Explanation 2:
First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221
'''

from collections import deque
class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        #11,22,1111,1221,2112,2222
        #basically - 1,2,11,12,21,22...
        q = deque(["1","2"])
        while A > 0:
            num = q.popleft()
            A -= 1
            for suffix in ["1","2"]:
                q.append(num+suffix)
        return num + num[::-1]

print(Solution().solve(5))