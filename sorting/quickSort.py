def quickSort(arr,beg,end):
    if beg < end:
        p = partition(arr,beg,end)
        quickSort(arr, beg, p-1)
        quickSort(arr, p+1, end)
    return arr

def partition(arr,beg,end):
    p = beg
    i,j = p,end
    while i < j:
        while i <= end and arr[i] <= arr[p]:
            i += 1
        while arr[j] > arr[p]:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[p],arr[j] = arr[j],arr[p]
    return j

arr = [1,3,42,33,3,55,11,9] 
print(quickSort(arr, 0, len(arr)-1))