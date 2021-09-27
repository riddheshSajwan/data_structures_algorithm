'''
https://www.geeksforgeeks.org/find-the-maximum-possible-value-of-ai-aj-over-all-pairs-of-i-and-j/
'''

'''
should always be = second_max_ele%max_ele
'''

def solve(A):
    if len(A) <= 1: return 0
    A.sort()
    i = 2
    while i <= len(A) and A[-i] == A[-1] : i += 1
    return A[-i]%A[-1] if i <= len(A) else 0 

print(solve([1, 2, 44, 3]))