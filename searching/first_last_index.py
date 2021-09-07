'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
def searchRange(arr, k):
    def first_index(k,idx,arr,beg,end):
        if beg <= end:
            mid = (beg+end)//2
            if k > arr[mid]:
                return first_index(k,idx,arr,mid+1,end)
            elif k == arr[mid]:
                idx = mid
            return first_index(k,idx,arr,beg,mid-1)
        return idx
            
    def second_index(k,idx,arr,beg,end):
        if beg <= end:
            mid = (beg+end)//2
            if k < arr[mid]:
                return second_index(k,idx,arr,beg,mid-1)
            elif k == arr[mid]:
                idx = mid
            return second_index(k,idx,arr,mid+1,end)
        return idx

    return [first_index(k,-1,arr,0,len(arr)-1),second_index(k,-1,arr,0,len(arr)-1)]

arr = [5,7,7,8,8,10]
k = 8
print(searchRange(arr, k))