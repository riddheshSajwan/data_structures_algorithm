'''
https://www.geeksforgeeks.org/maximum-of-xor-of-first-and-second-maximum-of-all-subarrays/
'''

def solve(A):
    max_xor = float('-inf')
    n = len(A)
    stack = [A[0]]
    for i in range(1,n):
        while stack:
            max_xor = max(max_xor,stack[-1]^A[i])
            if stack[-1] < A[i]:
                stack.pop()
            else:
                break
        stack.append(A[i])
    return max_xor 

A = [2, 3, 1, 4]
print(solve(A))