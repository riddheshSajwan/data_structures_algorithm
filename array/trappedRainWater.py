# https://leetcode.com/problems/trapping-rain-water/

def trap(height):

    if not height:
        return 0
      
    start,end = 0,len(height)-1
    right,left = height[start],height[end]
    area = 0
    
    while start < end:
        
      if height[start] < height[end] :
        start += 1
        right = max(right,height[start])
        area += right - height[start]
        
      else :
        end -= 1
        left = max(left,height[end])
        area += left - height[end]
        
      return area

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))