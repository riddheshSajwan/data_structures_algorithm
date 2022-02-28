'''
https://leetcode.com/problems/largest-rectangle-in-histogram/
'''

def largestRectangleArea(heights):
    stack = [-1]
    heights.append(0)
    ans = 0
    for i, height in enumerate(heights):
        while heights[stack[-1]] > height:
            h = heights[stack.pop()] 
            w = i - stack[-1] - 1
            ans = max(ans, h*w)
        stack.append(i)
    heights.pop()
    return ans

heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))