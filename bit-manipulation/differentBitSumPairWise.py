'''
https://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/
'''

def cntBits(A):
    n = len(A)
    res = 0
    pos = 0
    for pos in range(32):
        odd_count = 0
        for i in range(n):
            odd_count += 1 if A[i]&(1<<pos) > 0 else 0
        res += odd_count*(n-odd_count)*2

    return res

print(cntBits([1, 3, 5]))