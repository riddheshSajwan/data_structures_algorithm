'''
https://www.geeksforgeeks.org/check-if-each-internal-node-of-a-bst-has-exactly-one-child/
'''

def solve(A):
    low,high = float('-inf'),float('inf')
    node = A[0]
    for i in range(1,len(A)):
        if low < A[i] < high:
            if A[i] > node:
                low = node
            elif A[i] < node:
                high = node
            node = A[i]
        else:
            return "NO"
    return "YES"