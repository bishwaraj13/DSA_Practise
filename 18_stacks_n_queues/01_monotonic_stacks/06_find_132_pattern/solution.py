# https://leetcode.com/problems/132-pattern/
from typing import *

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minima = [0] * len(nums)
        minima[0] = nums[0]
        stack = []

        for i in range(1, len(nums)):
            minima[i] = min(nums[i], minima[i-1])

        # find prev greater at each index
        for i in range(len(nums)):
            while stack and nums[stack[-1]] <= nums[i]:
                stack_top = stack.pop()

            # if there is prev greater element, stack will not be empty
            if stack:
                # we found possible jth index
                possible_j = stack[-1]
                # now we need to see what was minimum at jth index
                min_at_j = minima[possible_j]

                if min_at_j < nums[i]:
                    return True

            stack.append(i)

        return False
    