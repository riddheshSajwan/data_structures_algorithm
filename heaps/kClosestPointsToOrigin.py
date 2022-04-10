'''
https://leetcode.com/problems/k-closest-points-to-origin/
'''

import heapq
class Solution:
    def kClosest(self, A, B):
        dist_arr = []
        points_map = {}
        for point in A:
            dist = point[0]**2 + point[1]**2
            if dist not in points_map:
                points_map[dist] = []
                dist_arr.append(dist)
            points_map[dist].append((point[0],point[1]))
        heapq.heapify(dist_arr)
        res = []
        #print(points_map[107650])
        count = B
        while count > 0:
            dist = heapq.heappop(dist_arr)
            for point in points_map[dist]:
                res.append([point[0],point[1]])
                #print(dist,point[0],point[1])
                count -= 1
                if count <= 0:
                    break

        #print(len(res))
        return res
    
print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))