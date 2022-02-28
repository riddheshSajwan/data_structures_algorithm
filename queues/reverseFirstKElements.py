'''
https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1/
'''
from collections import deque
def solve(A, B):
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

print(solve([5, 17, 100, 11], 2))