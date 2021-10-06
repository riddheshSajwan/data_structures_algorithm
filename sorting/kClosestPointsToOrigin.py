'''
https://leetcode.com/problems/k-closest-points-to-origin/
'''
def solve(A, B):
    '''A.sort(key = lambda key: key[0]**2 + key[1]**2)
    return A[:B]'''
    dist = []
    res = []
    for i in range(len(A)):
        dist.append([A[i],A[i][0]**2 + A[i][1]**2])
    dist.sort(key= lambda k : k[1])
    for item in dist[:B]:
        res.append(item[0])
    return res

A = [ 
       [1, 3],
       [-2, 2] 
     ]
B = 1

print(solve(A, B))