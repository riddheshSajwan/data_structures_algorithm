'''
https://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/
'''
def solve(A, B, C):
    res_i,res_j = 0,0
    i,j = 0,len(B)-1
    ans = float('inf')
    while i < len(A) and j > -1:
        #print(i,j,ans)
        pair_sum = A[i]+B[j]
        temp = abs(pair_sum-C)
        #print('temp',temp)
        if ans > temp:
            res_i = i
            res_j = j
            ans = temp
        elif ans == temp:
            res_i = min(res_i,i) if j == res_j else res_i
            res_j = min(res_j,j) if i == res_i else res_j
            #print('min',res_i,res_j)
        if pair_sum < C:
            i += 1
        elif pair_sum == C:
            return [A[i],B[j]]
        else:
            j -= 1
    return [A[res_i],B[res_j]]

A = [5, 10, 20]
B = [1, 2, 30]
C = 13
print(solve(A, B, C))