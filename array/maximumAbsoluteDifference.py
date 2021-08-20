def maxArr(A):
        #case1 = A[i] < A[j]. (A[j] + j) - (A[i] + i)
        #case2 = A[i] > A[j]. (A[i] - i) - (A[j] - j)
    max_case1 = max_case2 = float('-inf')
    min_case1 = min_case2 = float('inf')
    for i in range(len(A)):
        max_case1,min_case1 = max(max_case1,A[i]+i),min(min_case1,A[i]+i)
        max_case2,min_case2 = max(max_case2,A[i]-i),min(min_case2,A[i]-i)
    return max(max_case1-min_case1,max_case2-min_case2)

print(maxArr([1, 3, -1]))