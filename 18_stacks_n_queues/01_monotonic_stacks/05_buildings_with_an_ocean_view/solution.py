# https://leetcode.com/problems/buildings-with-an-ocean-view/
from typing import *

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # in other words, we want to find which of the buildings
        # have a next greater element
        # at the end, the elements left in the stack will be the ones
        # which wouldn't have any greater elements after them
        stack = []

        for i in range(len(heights)):
            # note the operator used is <=
            # because we want to pop out the buildings which have another
            # building with equal or greater height in view
            # this means the monotonic stack is goin to be strictly decreasing
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()

            stack.append(i)

        return stack