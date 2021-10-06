'''
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
'''
# TC - O(nlogn) SC - O(n)
def subUnsort(A):
    sorted_arr = [item for item in A]
    sorted_arr.sort()
    #print(A,sorted_arr)
    i = 0
    end = -1
    start = -1
    while i < len(A):
        if A[i] != sorted_arr[i]:
            end = i if start != -1 else -1
            start = i if start == -1 else start
            #print(i)
        i += 1
    return [-1] if start == -1 else [start,end]

print(subUnsort([1, 3, 2, 4, 5]))

# find the best solution