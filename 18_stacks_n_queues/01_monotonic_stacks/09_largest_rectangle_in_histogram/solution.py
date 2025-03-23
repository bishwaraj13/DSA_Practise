# https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import *

class Solution:
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