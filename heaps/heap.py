def heapify(arr,n,root):  
    left = 2*root + 1
    right = 2*root + 2
    smallest = root
    if left < n:
        smaller = left
        if right < n and arr[smaller] > arr[right]:
            smaller = right
        if arr[smaller] < arr[smallest]:
            arr[smaller],arr[smallest] = arr[smallest],arr[smaller]
            heapify(arr, n, smaller)
    return arr

def build_heap(arr,n):
    #last non-leaf node
    last_non_leaf = n//2 - 1
    while last_non_leaf >= 0:
        arr = heapify(arr,n,last_non_leaf)
        last_non_leaf -= 1
    return arr

def heap_sort(arr,n):
    arr = build_heap(arr, n)
    last_node = n-1
    while last_node > 0:
        arr[0],arr[last_node] = arr[last_node],arr[0]
        heapify(arr,last_node,0)
        last_node -= 1
    return arr

def insert(arr,n,node):
    arr.append(node)
    n += 1
    inserted_node = n-1
    inserted_node = (inserted_node-1)//2
    while inserted_node >= 0:
        arr = heapify(arr, n, inserted_node)
        inserted_node = (inserted_node-1)//2
    return arr,n

def delete(arr,n,index):
    arr[n-1],arr[index] = arr[index],arr[n-1]
    arr.pop()
    n = n - 1
    heapify(arr, n, index)
    return arr,n

def get_height(n):
    height = 1
    temp = n//2
    while temp:
        height += 1
        temp //= 2
    return height

arr = [4,3,5,9,7,3,1,0]
n = len(arr)
arr = build_heap(arr,n)
print("min-heap",arr)
arr,n = insert(arr, n, -1)
print("after-inserting",arr)
arr,n = delete(arr, n, 1)
print("after-deleting",arr)
print("after-sorting",heap_sort(arr,n))
