"""
    Container With Most Water
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.
    
"""

class Solution:
    def maxArea(self, height):
        h = 0
        w = len(height) - 1
        max_water = 0

        while h < w:
            area = (w - h) * min(height[h], height[w])

            if area > max_water:
                max_water = area
            
            if height[h] < height[w]:
                h += 1
            else:
                w -= 1
            
        return max_water

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))
