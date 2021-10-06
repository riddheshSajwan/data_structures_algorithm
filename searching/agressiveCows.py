'''
Aggressive cows
Problem Description

Farmer John has built a new long barn, with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall, and an integer B which represent the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

Example Input
Input 1:

A = [1, 2, 3, 4, 5]
B = 3
Input 2:

A = [1, 2]
B = 2


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 
John can assign the stalls at location 1,3 and 5 to the 3 cows respectively.
So the minimum distance will be 2.
Explanation 2:

 
The minimum distance will be 1.
'''

def solve(A, B):
    # search space is 0 to max(A)-min(A)
    n = len(A)
    A.sort()
    #print(A)
    def check(dist):
        pos = A[0]
        i = 0
        itr = 0
        while itr < B-1:
            while A[i] < pos + dist:
                i += 1
                if i >= n :
                    return False
            pos = A[i]
            itr += 1
        return True
    beg,end = 0,A[-1]-A[0]
    ans = 0
    while beg <= end :
        mid = beg + (end-beg)//2
        #print(beg,end,mid,ans)
        if check(mid):
            ans = mid
            beg = mid + 1
        else:
            end = mid - 1
    return ans

print(solve([1, 2, 3, 4, 5], 3))