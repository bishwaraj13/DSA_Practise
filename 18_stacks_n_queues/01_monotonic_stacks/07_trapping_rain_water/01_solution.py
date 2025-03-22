# https://leetcode.com/problems/trapping-rain-water/description/
from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
    
        n = len(height)
        
        # Initialize arrays to store the maximum height to the left and right of each position
        max_left = [0] * n
        max_right = [0] * n
        
        # Fill max_left array
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])
        
        # Fill max_right array
        max_right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])
        
        # Calculate trapped water at each position
        total_water = 0
        for i in range(n):
            # Water trapped = min(max_left, max_right) - current_height
            water_at_position = min(max_left[i], max_right[i]) - height[i]
            if water_at_position > 0:
                total_water += water_at_position
        
        return total_water