# https://leetcode.com/problems/house-robber/
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(index):
            if index == 0:
                return nums[0]

            if index < 0:
                return 0

            # include current house
            left = nums[index] + dfs(index - 2)

            # dont include current house
            right = dfs(index - 1)

            return max(left, right)

        return dfs(len(nums) - 1)