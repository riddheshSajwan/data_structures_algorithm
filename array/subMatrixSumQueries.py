def solve(A, B, C, D, E):
    n = len(A)
    m = len(A[0])
    res = []
    prefix = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            prefix[i][j] = A[i][j]
            if i-1 >= 0 :
                prefix[i][j] += prefix[i-1][j]
            if j-1 >= 0 :
                prefix[i][j] += prefix[i][j-1]
            if i-1 >= 0 and j-1 >= 0 :
                prefix[i][j] -= prefix[i-1][j-1]
    for i in range(len(B)):
        li = B[i]-1
        lj = C[i]-1
        ri = D[i]-1
        rj = E[i]-1
        temp_sum = prefix[ri][rj]%1000000007
        if li-1 >= 0:
            temp_sum -= prefix[li-1][rj]%1000000007
        if lj-1 >= 0:
            temp_sum -= prefix[ri][lj-1]%1000000007
        if li-1 >= 0 and lj-1 >= 0:
            temp_sum += prefix[li-1][lj-1]%1000000007
        res.append(temp_sum%1000000007)
    return res

A = [   [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]  ]
B = [1, 2]
C = [1, 2]
D = [2, 3]
E = [2, 3]
print(solve(A, B, C, D, E))