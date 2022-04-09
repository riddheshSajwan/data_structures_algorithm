'''
https://www.geeksforgeeks.org/reversing-first-k-elements-queue/
'''

from collections import deque
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        if n < 2:
            return A
        q = deque()
        for i in range(B):
            q.append(A[i])
        i = B - 1
        while len(q) != 0:
            A[i] = q.popleft()
            i -= 1
        return A

print(Solution().solve([5, 17, 100, 11], 2))