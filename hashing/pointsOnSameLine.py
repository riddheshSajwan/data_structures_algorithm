'''
https://leetcode.com/problems/max-points-on-a-line/
'''
def _gcd(a,b):
    if a == 0:
        return b
    return _gcd(b%a,a)
def maxPoints(points) -> int:
    A,B = [],[]
    for item in points:
        A.append(item[0])
        B.append(item[1])
    n = len(A)
    globalMax = 1
    for i in range(n):
        slope_map = {}
        currMax = float('-inf')
        overlap = 0
        for j in range(i+1,n):
            x = A[i]-A[j]
            y = B[i]-B[j]
            if y == 0 and x == 0:
                overlap += 1
                continue
            else:
                red = _gcd(x,y)
                # if red == 0:
                #     print(A[i],A[j],B[i],B[j],red)
                slope = str(y//red) + "/" + str(x//red)
            #if slope == '-1/2': print(A[i],A[j],B[i],B[j])
            if slope not in slope_map:
                slope_map[slope] = 1
            slope_map[slope] += 1
            currMax = max(currMax,slope_map[slope])
        globalMax = max(globalMax,currMax+overlap)
        #print(slope_map)

    return globalMax

print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))