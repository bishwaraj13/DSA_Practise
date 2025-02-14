# https://leetcode.com/problems/jump-game-ii/
# Wont be able to come to this solution myself
# https://www.youtube.com/watch?v=7SBVnw7GSTk
from typing import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = 0
        r = 0

        while r < len(nums) - 1:
            farthest = 0

            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])

            l = r+1
            r = farthest
            jumps = jumps + 1

        return jumps