'''
https://leetcode.com/problems/single-number-ii/
'''
def singleNumber(A):
    res = 0
    for bit in range(32):
        count = 0
        for i in range(len(A)):
            count += 1 if A[i]&(1<<bit) > 0 else 0
        res += count%3<<bit
    return res

print(singleNumber([1, 2, 4, 3, 3, 2, 2, 3, 1, 1]))