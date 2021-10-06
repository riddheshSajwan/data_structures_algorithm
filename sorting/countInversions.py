'''
https://www.geeksforgeeks.org/counting-inversions/
'''

def solve(A):
    def mergeSort(beg,end,count):
        if beg < end:
            mid = beg + (end-beg)//2
            #print(beg,end,mid)
            a = mergeSort(beg,mid,count)
            b = mergeSort(mid+1,end,count)
            count += a + b + merge(beg,mid,end)
            #print(a,b,count)
        return count
    def merge(beg,mid,end):
        count = 0
        k = beg
        L,R = A[beg:mid+1],A[mid+1:end+1]
        i,j = 0,0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                count += len(L)-i
                A[k] = R[j]
                j += 1
            else:
                A[k] = L[i]
                i += 1
            k += 1
        if i < len(L):
            A[k:end+1] = L[i:]
        if j < len(R):
            A[k:end+1] = R[j:]
        #print(L,R,count)
        return count
    return mergeSort(0,len(A)-1,0)%1000000007

print(solve([3, 2, 1]))
                    
                    