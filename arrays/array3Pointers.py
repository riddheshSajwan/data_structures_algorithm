'''
https://www.interviewbit.com/problems/array-3-pointers/
'''

def minimize(A, B, C):
    ans = float('inf')
    i,j,k = 0,0,0
    ni,nj,nk = len(A),len(B),len(C)
    while i < ni and j < nj and k < nk:
        bigger = max(A[i],B[j],C[k])
        smaller = min(A[i],B[j],C[k])
        ans = min(ans,bigger-smaller)
        if ans == 0:
            return 0
        if smaller == A[i]:
            i += 1
        elif smaller == B[j]:
            j += 1
        else:
            k += 1
    return ans

A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]
print(minimize(A, B, C))