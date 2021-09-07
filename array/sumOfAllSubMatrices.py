def solve(A):
    n = len(A)
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += A[i][j]*(j+1)*(i+1)*(n-j)*(n-i)
    return sum
A = [ [1, 1],[1, 1] ]
print(solve(A))