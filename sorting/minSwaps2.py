'''
Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)]. It is allowed to swap any two elements (not necessarily consecutive).

Find the minimum number of swaps required to sort the array in ascending order.
'''

def solve(A):
    swap_count = 0
    i = 0
    while i < len(A):
        if A[i] != i:
            temp = A[i]
            A[temp],A[i] = A[i], A[temp]
            swap_count += 1
        else:
            i += 1
    return swap_count

print(solve([2, 0, 1, 3]))