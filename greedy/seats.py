'''
https://www.interviewbit.com/problems/seats/
'''

class Solution:
	# @param A : string
	# @return an integer
    def seats(self, A):
        pos = []
        for i in range(len(A)):
            if A[i] == "x":
                pos.append(i)
        m = len(pos)
        if m == 0:
            return 0
        median = m//2
        left,right = pos[median]-1, pos[median]+1
        res = 0
        k = median-1
        #print(pos,median,left,right)
        while k >=0 :
            res += left - pos[k]
            k -= 1
            left -= 1
        k = median + 1
        while k < m:
            res += pos[k] - right
            right += 1
            k += 1
        return res%int(1e7+3)

print(Solution().seats("....x..xx...x.."))