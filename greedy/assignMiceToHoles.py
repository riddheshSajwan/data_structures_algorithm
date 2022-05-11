'''
https://www.interviewbit.com/problems/assign-mice-to-holes/
'''

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()
        res = 0
        for i in range(len(A)):
            res = max(res,abs(A[i]-B[i]))
        return res

print(Solution().mice([-4, 2, 3], [0, -2, 4]))