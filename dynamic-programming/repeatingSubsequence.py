'''
https://www.interviewbit.com/problems/repeating-subsequence/
'''

def anytwo(A):
    B = A
    m = len(A)
    prev = [0]*(m+1)
    curr = [0]*(m+1)
    #print(dp)
    for i in range(m-1,-1,-1):
        for j in range(m-1,-1,-1):
            if A[i] == B[j] and i != j:
                curr[j] = 1 + prev[j+1]
            else:
                curr[j] = max(curr[j+1], prev[j])
        for j in range(m+1):
            prev[j] = curr[j]
    return 1 if curr[0] >= 2 else 0

print(anytwo("abab"))