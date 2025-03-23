# https://leetcode.com/problems/maximal-rectangle/
# This solution uses the function we created at largest_rectangle_in_histogram
from typing import *

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in range(rows):
            # Update heights based on current row
            for col in range(cols):
                if matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0
            
            # Calculate max rectangle area for current histogram
            current_max_area = self.largestRectangleArea(heights)
            max_area = max(max_area, current_max_area)
        
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        prev_smaller = [-1] * len(heights)
        next_smaller = [len(heights)] * len(heights)
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack_top = stack.pop()
                next_smaller[stack_top] = i

            if stack:
                prev_smaller[i] = stack[-1]

            stack.append(i)

        for i in range(len(heights)):
            width = next_smaller[i] - prev_smaller[i] - 1
            ht = heights[i]
            max_area = max(max_area, width * ht)

        return max_area
        