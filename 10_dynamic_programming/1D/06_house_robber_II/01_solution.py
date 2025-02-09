# https://leetcode.com/problems/house-robber-ii/

# the solution is built on top of house robber - I, and its just one wrapper of small hack
from typing import List

class Solution:
    # could replace this function with top-down or bottom-up
    # from house robber-i and it will still work
    def maximum_adjacent_sum(self, nums: List[int]) -> int:
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

        return dfs(len(nums)-1)

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        return max(
            self.maximum_adjacent_sum(nums[0:len(nums)-1]),
            self.maximum_adjacent_sum(nums[1:len(nums)])
        )