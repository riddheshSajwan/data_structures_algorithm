'''
https://leetcode.com/problems/combination-sum/
'''

def combinationSum(A, B):
    ans = []
    temp = []
    A = sorted(list(set(A)))
    
    def findNumbers(ans, arr, temp, sum, index):
    
        if(sum == 0):
            ans.append(list(temp))
            return

        for i in range(index, len(arr)):

            if(sum - arr[i]) >= 0:
                temp.append(arr[i])
                findNumbers(ans, arr, temp, sum-arr[i], i)
                temp.remove(arr[i])
    
    findNumbers(ans, A, temp, B, 0)
    return ans

print(combinationSum([2,3,6,7], 7))