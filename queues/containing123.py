'''
Problem Description
Given an integer A. Find and Return first positive A integers in ascending order containing only digits 1, 2 and 3.
NOTE: All the A integers will fit in 32 bit integer.

Problem Constraints
1 <= A <= 29500

Input Format
The only argument given is integer A.

Output Format
Return an integer array denoting the first positive A integers in ascending order containing only digits 1, 2 and 3.

Example Input
Input 1:
 A = 3
Input 2:
 A = 7

Example Output
Output 1:
 [1, 2, 3]
Output 2:
 [1, 2, 3, 11, 12, 13, 21]

Example Explanation
Explanation 1:
 Output denotes the first 3 integers that contains only digits 1, 2 and 3.
Explanation 2:
 Output denotes the first 3 integers that contains only digits 1, 2 and 3.
 '''

from collections import deque
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        res = []
        if A <= 3:
            for i in range(1,A+1):
                res.append(i)
            return res
        q = deque([1,2,3])
        while A > 0:
            num = q.popleft()
            res.append(num)
            A -= 1
            for suffix in ["1","2","3"]:
                q.append(int(str(num)+suffix))
        return res

print(Solution().solve(5))