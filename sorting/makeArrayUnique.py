'''
https://leetcode.com/problems/minimum-increment-to-make-array-unique/
'''

'''
add one to every duplicate until it becomes unique. Use sorting and caching to improve TC.
'''

def minIncrementForUnique(A):
    cache = {}
    res = 0
    A.sort()
    last = 0
    for i in range(len(A)):
        if A[i] in cache:
            res += last - A[i]
            A[i] = last
            while A[i] in cache:
                A[i] += 1
                res += 1
        last = A[i]
        cache[A[i]] = True
    return res

print(minIncrementForUnique([3,2,1,2,1,7]))