'''
Problem Description
You are given an array A containing N numbers. This array is called special if it satisfies one of the following properties:
There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[0], A[1], ...., A[i-1]]
There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[i+1], A[i+2], ...., A[N-1]]
The Median is the middle element in the sorted list of elements. If the number of elements is even then the median will be (sum of both middle elements) / 2.
Return 1 if the array is special else return 0.

NOTE:
For A[0] consider only the median of elements [A[1], A[2], ..., A[N-1]] (as there are no elements to the left of it)
For A[N-1] consider only the median of elements [A[0], A[1], ...., A[N-2]]

Problem Constraints
1 <= N <= 1000000.
A[i] is in the range of a signed 32-bit integer.

Input Format
The first and only argument is an integer array A.

Output Format
Return 1 if the given array is special else return 0.

Example Input
Input 1:
 A = [4, 6, 8, 4]
Input 2:
 A = [2, 7, 3, 1]

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explantion 1:
 Here, 6 is equal to the median of [8, 4].
Explanation 2:
 No element satisfies any condition.
 '''

from heapq import heappush,heappop
class Solution:
    # @param A : list of integers
    # @return a list of integers

    def get_med_arr(self,A):
        minheap,maxheap = [],[]
        minheap_size,maxheap_size = 0,0
        res = []
        median = float('inf')
        for item in A:
            if item <= median:
                if maxheap_size > minheap_size:
                    heappush(minheap,-heappop(maxheap))
                    minheap_size += 1
                    maxheap_size -= 1
                heappush(maxheap,-item)
                maxheap_size += 1
            else:
                if minheap_size > maxheap_size:
                    heappush(maxheap,-heappop(minheap))
                    maxheap_size += 1
                    minheap_size -= 1
                heappush(minheap,item)
                minheap_size += 1
            if maxheap_size > minheap_size:
                median = -maxheap[0]
            elif minheap_size == maxheap_size:
                median = (-maxheap[0] + minheap[0])/2
            else:
                median = minheap[0]
            res.append(median)
        return res

    def solve(self, A):
        n = len(A)
        res,res_rev = self.get_med_arr(A), self.get_med_arr(A[::-1])
        #print(res,res_rev)
        for i in range(1,n):
            if A[i] == res[i-1]:
                return 1
        A.reverse()
        for i in range(1,n):
            if A[i] == res_rev[i-1]:
                return 1
        return 0
print(Solution().solve([4, 6, 8, 4]))