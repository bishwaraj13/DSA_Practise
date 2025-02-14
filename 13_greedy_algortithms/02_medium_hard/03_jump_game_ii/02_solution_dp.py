# https://leetcode.com/problems/jump-game-ii/
# the following code has an issue
# initialization of cache is problem because we dont know size of m x n array
from typing import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # Create a 2D cache initialized with -1
        # First dimension: index, Second dimension: jumps taken so far
        cache = [[-1] for _ in range(n)]
        def recursively_jump(index, jumps):
            if index >= len(nums)-1:
                return jumps

            # Check if this state (index, jumps) has been computed before
            if cache[index][jumps] != -1:
                return cache[index][jumps]

            mini = float("inf")

            for i in range(1, nums[index]+1):
                mini = min(mini, recursively_jump(index+i, jumps+1))

            # Store the result for this (index, jumps) combination
            cache[index][jumps] = mini

            return mini

        return recursively_jump(0, 0)