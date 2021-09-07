'''
https://leetcode.com/problems/rotate-image/
'''
def rotate(A):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(A)
        m = n-1
        res = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                res[j][m-i] = A[i][j]
        for i in range(n):
            for j in range(n):
                A[i][j] = res[i][j]
        return A
print(rotate([[1,2,3],[4,5,6],[7,8,9]]))