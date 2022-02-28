'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''
def maxArea(height):
      
    maxVal = max(height)
    start = 0 
    end = len(height) - 1
    maxArea = 0
      
    while maxArea < (end-start)*maxVal :
        maxArea = max(maxArea,(end-start)*min(height[end],height[start]))
        if height[start] > height[end]:
            end-=1
        elif height[start] < height[end]:
            start+=1
        else:
            start+=1
            end-=1
          
    return maxArea

print(maxArea([1,8,6,2,5,4,8,3,7]))