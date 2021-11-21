'''
https://www.geeksforgeeks.org/count-rectangles-generated-in-a-given-rectangle-by-lines-drawn-parallel-to-x-and-y-axis-from-a-given-set-of-points/
'''

def solve(A, B):
    res = 0
    n = len(A)
    points = {(A[i],B[i]):True for i in range(n)}
    #print(points)
    for i in range(n):
        for j in range(i+1,n):
            if A[i] != A[j] and B[i] != B[j]  \
            and (A[i],B[j]) in points and (A[j],B[i]) in points:
                #print(A[i],B[i],A[j],B[j])
                res += 1
    #print("res ",res)
    return res//2

A = [1, 1, 2, 2, 3, 3] # x-coordinates
B = [1, 2, 1, 2, 1, 2] # y-coordinates
print(solve(A, B))