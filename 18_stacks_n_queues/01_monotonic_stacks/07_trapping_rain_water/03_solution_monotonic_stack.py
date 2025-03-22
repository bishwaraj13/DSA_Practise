# https://leetcode.com/problems/trapping-rain-water/description/
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # 1. We iterate through the height array
        # 2. We maintain a stack of indices where the heights are in non-increasing order (find next-greater)
        # 3. When we find a bar taller than the one at the top of the stack, 
        # we can trap water between them We calculate the trapped water and add it to our total
        # 4. 3 is done by popping the stack.. this is the index where we want to see how much water we trapped because of the right bar.
        stack = []
        total_water = 0

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                middle_index = stack.pop()

                if stack:
                    left_boundary_index = stack[-1]
                    left_ht = height[left_boundary_index]

                    ht_of_water = min(left_ht, height[i]) - height[middle_index]
                    width = i - left_boundary_index - 1

                    total_water += (ht_of_water * width)

            stack.append(i)

        return total_water