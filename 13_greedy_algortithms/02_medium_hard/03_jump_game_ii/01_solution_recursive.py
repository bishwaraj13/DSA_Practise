# https://leetcode.com/problems/jump-game-ii/
# this is brute force approach
from typing import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        def recursively_jump(index, jumps):
            if index >= len(nums)-1:
                return jumps

            mini = float("inf")

            for i in range(1, nums[index]+1):
                mini = min(mini, recursively_jump(index+i, jumps+1))

            return mini

        return recursively_jump(0, 0)