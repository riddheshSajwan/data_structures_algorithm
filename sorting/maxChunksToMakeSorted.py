'''
https://leetcode.com/problems/max-chunks-to-make-sorted/
'''

def solve(A):
    res = 0
    num = -1
    idx = 0
    while idx < len(A):
        num = max(num,A[idx])
        if idx == num:
            res += 1
            num += 1
        idx += 1
    return res

print(solve([1, 2, 3, 4, 0]))