def merge_sort(arr,beg,end): 
    if beg < end: 
        mid = (beg+end)//2
        merge_sort(arr,beg,mid) 
        merge_sort(arr,mid+1,end) 
        merge(arr,beg,mid,end)
    return arr 

def merge(arr,beg,mid,end): 
    k = beg 
    L = arr[beg:mid+1] 
    R = arr[mid+1:end+1] 
    i = j = 0 
    while i < len(L) and j < len(R): 
        if L[i] < R[j]: 
            arr[k] = L[i]
            i+=1 
        else: 
            arr[k] = R[j] 
            j+=1 
        k+=1
    if i < len(L):
        arr[k:end+1] = L[i:]
    if j < len(R):
        arr[k:end+1] = R[j:]

arr = [1,3,42,33,4,55,11,9] 
print(merge_sort(arr,0,len(arr)-1))