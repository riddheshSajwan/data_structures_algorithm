'''
https://leetcode.com/problems/next-permutation/
'''
def nextPermutation(A):
    i = j = len(A)-1
    while i > 0 and A[i-1] >= A[i]:
        i -= 1
    if i == 0:   # A are in descending order
        A.reverse()
        return A
    k = i - 1    # find the last "ascending" position
    while A[j] <= A[k]:
        j -= 1
    A[k], A[j] = A[j], A[k]  
    l, r = k+1, len(A)-1  # reverse the second part
    while l < r:
        A[l], A[r] = A[r], A[l]
        l +=1 ; r -= 1
    return A

print(nextPermutation([1,2,3]))