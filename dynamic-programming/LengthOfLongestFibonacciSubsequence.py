'''
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/
'''

def lenLongestFibSubseq(arr):
    s=set(arr)
    res=0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            total=2
            prev,cur=arr[i],arr[j]
            while prev+cur in s:
                total+=1
                prev,cur=cur,prev+cur
            res=max(res,total)
    return res if res>2 else 0

print(lenLongestFibSubseq([1,3,7,11,12,14,18]))