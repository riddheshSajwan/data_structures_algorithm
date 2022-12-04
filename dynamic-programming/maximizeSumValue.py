'''
https://www.geeksforgeeks.org/given-array-three-numbers-maximize-x-ai-y-aj-z-ak/
'''
import sys

def maximizeExpr(a, n, x, y, z):
 
    # Traverse the whole array
    # and compute left maximum
    # for every index.
    L = [0] * n
    L[0] = x * a[0]
    for i in range(1, n):
        L[i] = max(L[i - 1], x * a[i])
 
    # Compute right maximum
    # for every index.
    R = [0] * n
    R[n - 1] = z * a[n - 1]
    for i in range(n - 2, -1, -1):
        R[i] = max(R[i + 1], z * a[i])
 
    # Traverse through the whole
    # array to maximize the
    # required expression.
    ans = -sys.maxsize
    for i in range(0, n):
        ans = max(ans, L[i] + y *
                       a[i] + R[i])
 
    return ans

a = [-1, -2, -3, -4, -5]
n = len(a)
x = 1
y = 2
z = -3

print(maximizeExpr(a, n, x, y, z))