# https://leetcode.com/problems/house-robber/
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_cache = [float('-inf')] * len(nums)

        def dfs(index):
            if index == 0:
                return nums[0]

            if index < 0:
                return 0

            if dp_cache[index] != float('-inf'):
                return dp_cache[index]

            # include current house
            left = nums[index] + dfs(index - 2)

            # dont include current house
            right = dfs(index - 1)

            dp_cache[index] = max(left, right)
            return dp_cache[index]

        return dfs(len(nums) - 1)
    