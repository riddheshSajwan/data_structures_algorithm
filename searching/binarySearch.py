def binary_search(key,arr,beg,end):
    if beg <= end:
        mid = (beg+end)//2
        if key > arr[mid]:
            return binary_search(key, arr, mid+1, end)
        elif key < arr[mid]:
            return binary_search(key, arr, beg, mid-1)
        elif key == arr[mid]:
            return mid
    return -1

def binary_search2(key,arr,beg,end):
    while beg <= end:
        mid = (beg+end)//2
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            beg = mid + 1
        elif key < arr[mid]:
            end = mid - 1
    return -1

arr = [1,3,3,5,6,7,8,12,15,15,36,78,99]
print(binary_search(33, arr, 0, len(arr)-1))
print(binary_search2(33, arr, 0, len(arr)-1))