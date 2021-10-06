'''
https://leetcode.com/problems/combination-sum-ii/
'''
def combinationSum(A, B):
    res = []
    n = len(A)
    A.sort()
    visited_idx = {i:False for i in range(n)}
    def _comb(idx,_res,sum,_visited_idx):
        if sum == B:
            res.append(_res)
            return
        if sum > B: return
        _visited = set()
        for i in range(idx,n):
            if not _visited_idx[i] and A[i] not in _visited:
                _visited_idx[i] = True
                _visited.add(A[i])
                _comb(i+1,_res+[A[i]],sum+A[i],_visited_idx)
                _visited_idx[i] = False
    _comb(0,[],0,visited_idx)
    return res

print(combinationSum([10, 1, 2, 7, 6, 1, 5], 8))