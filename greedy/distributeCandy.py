'''
https://www.interviewbit.com/problems/distribute-candy/
'''

class Solution:
	# @param A : list of integers
	# @return an integer
    def candy(self, ratings):
        gifts = [1]*len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i+1]>ratings[i]:
                if gifts[i+1]<gifts[i]:
                    gifts[i+1] += (gifts[i]-gifts[i+1])+1
                elif gifts[i+1] == gifts[i]:
                    gifts[i+1] += 1
        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1]>ratings[i]:
                if gifts[i-1]<gifts[i]:
                    gifts[i-1] += (gifts[i]-gifts[i-1])+1
                elif gifts[i-1] == gifts[i]:
                    gifts[i-1] += 1
        return sum(gifts)

print(Solution().candy([1, 5, 2, 1]))