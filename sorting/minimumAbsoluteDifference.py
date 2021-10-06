'''
https://www.geeksforgeeks.org/find-minimum-difference-pair/
'''
def solve(A):
    min_diff = float('inf')
    A.sort()
    for i in range(1,len(A)):
        min_diff = min(min_diff,abs(A[i]-A[i-1]))
    return min_diff

print(solve([5,17,100,11]))