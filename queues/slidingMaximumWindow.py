'''
https://leetcode.com/problems/sliding-window-maximum/
'''

def slidingMaximum(arr, k):
    i, j = 0, 0
    maxi = 0
    q, ans = [], []
    
    while j < len(arr):
    
        while len(q) > 0 and q[-1] < arr[j]:
            q.pop()
        q.append(arr[j])
    
        if (j - i + 1) == k:
    
            ans.append(q[0])
    
            if q[0] == arr[i]:
                q.pop(0)
    
            i += 1
            j += 1
    
        elif (j - i + 1) < k:
            j += 1
    
    return (ans)

print(slidingMaximum([1, 3, -1, -3, 5, 3, 6, 7], 3))