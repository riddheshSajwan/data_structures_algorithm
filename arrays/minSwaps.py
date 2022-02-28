'''
https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1#
'''
# TC = O(N), SC = O(N) 
def min_swap(A, B):
    bad_count_array = [0]
    bad_count = 0
    for i in range(len(A)):
        if A[i] > B:
            bad_count += 1
        bad_count_array.append(bad_count)
    good_count = len(A) - bad_count
    i = 1
    j = good_count
    min_swap = float('inf')
    while j < len(bad_count_array):
        min_swap = min(bad_count_array[j] - bad_count_array[i-1],min_swap)
        j += 1
        i += 1
    return min_swap

# TC = O(N), SC = O(1) 
def min_swap2(A,n,B):
    good_count = 0
    for i in range(n):
        if A[i] <= B:
            good_count += 1
    i = 0
    j = good_count-1
    min_swap = 0
    for k in range(i,j+1):
        if A[k] > B:
            min_swap += 1
    i += 1
    j += 1
    temp = min_swap
    while j < n :
        if A[i-1] > B:
            temp -= 1
        if A[j] > B:
            temp += 1
        min_swap = min(temp,min_swap)
        i += 1
        j += 1
    return min_swap

A = [1, 12, 10, 3, 14, 10, 5]
B = 8
print(min_swap(A, B))
print(min_swap2(A, len(A), B))