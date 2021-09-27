'''
Game of Bottles
Problem Description

Given an array of integers A of size N which denotes N cylindrical empty bottles. The radius of the ith bottle is A[i].
You can put the ith bottle into the jth bottle if the following conditions are met:

ith bottle is not put into another bottle.
jth bottle dosen't contain any other bottle.
The radius of bottle i is smaller than bottle j (A[i] < A[j]).
You can put bottles into each other any number of times. You want to MINIMIZE the number of visible bottles. A bottle is called visible if it is not put into any other bottle.

Find and return the minimum number of visible bottles.
'''

def solve(A):
    invisible_count = 0
    A.sort()
    i,j = 0,1
    n = len(A)
    while i < n and j < n:
        if A[i] < A[j]:
            A[i] = -1
            invisible_count += 1
            i += 1
        j += 1
    return n - invisible_count

print(solve([1,2,3]))