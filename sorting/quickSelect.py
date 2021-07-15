'''
https://leetcode.com/problems/kth-largest-element-in-an-array/
'''
def quickSelect(nums,beg,end):
    if beg < end:
        p = partition(nums,beg,end)
        if p == k:
            return nums[k]
        elif p < k:
            return quickSelect(nums,p+1,end)
        return quickSelect(nums,beg,p-1)
    return nums[k]
      
def partition(nums,beg,end):
    p = beg
    pivot = nums[p]
    while beg < end:
        while beg < len(nums) and nums[beg] >= pivot:
            beg += 1
        while nums[end] < pivot:
            end -= 1
        if beg < end:
            nums[beg],nums[end] = nums[end],nums[beg]
    nums[p],nums[end] = nums[end],nums[p]
    return end

nums = [3,2,3,1,2,4,5,5,6]
k = 4
k = k-1
print(quickSelect(nums,0,len(nums)-1))