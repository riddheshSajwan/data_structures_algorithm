'''
https://www.geeksforgeeks.org/count-of-right-angled-triangle-formed-from-given-n-points-whose-base-or-perpendicular-are-parallel-to-x-or-y-axis/
'''

def solve(A, B):
    MOD = int(1e9+7)
    res = 0
    n = len(A)           
    mx,my = {},{}
    for i in range(n):
        if A[i] not in mx:
            mx[A[i]] = 0
        if B[i] not in my:
            my[B[i]] = 0
        mx[A[i]] += 1
        my[B[i]] += 1
    for i in range(n):
        res += (mx[A[i]]-1)*(my[B[i]]-1)%MOD
        res %= MOD
    return res

A = [1, 1, 2, 3, 3] # x-coordinates
B = [1, 2, 1, 2, 1] # y-coordinates

print(solve(A, B))

