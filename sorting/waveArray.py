'''
https://www.geeksforgeeks.org/sort-array-wave-form-2/
'''

def wave(A):
    A.sort()
    for i in range(0,len(A)-1,2):
        A[i],A[i+1] = A[i+1],A[i]
    return A

print(wave([1,2,3,4]))