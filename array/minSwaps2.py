'''https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/'''

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