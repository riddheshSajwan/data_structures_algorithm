'''
https://www.interviewbit.com/problems/max-continuous-series-of-1s/
'''

def maxone(A, B):
    rem = B
    final_left = 0
    final_right = 0
    i,j = 0,0
    res = 0
    max_res = float('-inf')
    while j < len(A):
        if i > j:
            j += 1
            continue
        if rem >= 0:
            rem -= 1 - A[j]
            res += 1
            if rem >= 0 and res > max_res:
                max_res = res
                final_left = i
                final_right = j
        else:
            rem += 1 - A[i]
            i += 1
            res -= 1
            continue
        j += 1
    return [idx for idx in range(final_left,final_right+1)]

A = [1,1,0,1,1,0,0,1,1,1]
B = 1
print(maxone(A, B))