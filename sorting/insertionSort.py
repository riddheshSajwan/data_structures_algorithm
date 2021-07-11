def insertion_sort(arr): 
    for i in range(1,len(arr)): 
        key = arr[i] 
        j = i-1 
        while arr[j] > key and j >= 0: 
            arr[j+1] = arr[j] 
            arr[j] = key 
            j -= 1 
    return arr 

print(insertion_sort([1,3,42,33,4,55,11,9])) 