'''
https://leetcode.com/problems/maximal-rectangle/description/
'''

class Solution:

    def largestHistogramArea(self, heights):
        stack = [-1]
        heights.append(0)
        ans = 0
        for i, height in enumerate(heights):
            while heights[stack[-1]] > height:
                h = heights[stack.pop()] 
                w = i - stack[-1] - 1
                ans = max(ans, h*w)
            stack.append(i)
        heights.pop()
        return ans

    def maximalRectangle(self, matrix):
        A = [[0]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(A)):
          for j in range(len(A[0])):
            A[i][j] = int(matrix[i][j])
        res = float('-inf')
        histogram_mat = [[item for item in A[0]]] + [[0]*len(A[0]) for i in range(1,len(A))]
        for i in range(1,len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    histogram_mat[i][j] = A[i][j] + histogram_mat[i-1][j]
        #print(histogram_mat)
        for row in histogram_mat:
            res = max(res,self.largestHistogramArea(row))
        return res

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalRectangle(matrix))