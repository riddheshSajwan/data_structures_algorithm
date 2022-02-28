'''https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/'''

def maximumGap(A):
    if len(A) == 1:
        return 0
    min_arr = [0 for i in range(len(A))]
    max_arr = [len(A)-1 for i in range(len(A))]
    min_arr[0] = A[0]
    for i in range(1,len(min_arr)):
        if A[i] < min_arr[i-1]:
            min_arr[i] = A[i]
        else:
            min_arr[i] = min_arr[i-1]
    max_arr[-1] = A[-1]
    for i in range(len(max_arr)-2,-1,-1):
        if A[i] > max_arr[i+1]:
            max_arr[i] = A[i]
        else:
            max_arr[i] = max_arr[i+1]
    i = j = 0
    ret = -1
    while i < len(A) and j < len(A):
        if min_arr[i] <= max_arr[j]:
            ret = max(ret, j-i)
            j += 1
        else:
            i += 1
    return ret

print(maximumGap([3, 5, 4, 2]))