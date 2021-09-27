'''
https://leetcode.com/problems/merge-sorted-array/
'''

# with extra space.
def solve(A, B):
    n = len(A)
    m = len(B)
    res = []
    i,j = 0,0
    while i < n and j < m:
        
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
        #print(res,i,j)
    if i < n:
        res += A[i:]
    if j < m:
        res += B[j:]
    return res

print(solve([4,7,9], [2,11,19]))

# Without extra space
def merge(nums1,m,nums2,n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]
    return nums1
print(merge([4,7,9,'','',''],3,[2,11,19],3))