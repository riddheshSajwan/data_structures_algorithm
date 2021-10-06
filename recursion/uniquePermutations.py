'''
https://leetcode.com/problems/permutations-ii/
'''

def permute(A):
    perms = []
    n = len(A)
    def _permute(arr,_perm,usedVal = set()):
        if len(_perm) == n:
            perms.append(_perm)
            return
        usedVal = set()
        for i in range(len(arr)):
            if arr[i] not in usedVal:
                usedVal.add(arr[i])
                _permute(arr[:i]+arr[i+1:],_perm+[arr[i]],usedVal)
    _permute(A,[])
    return perms
print(permute([1,1,2]))