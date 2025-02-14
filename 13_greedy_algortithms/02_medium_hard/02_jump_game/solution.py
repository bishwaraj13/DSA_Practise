# https://leetcode.com/problems/jump-game
# Hard to come up with this solution intuitively using Greedy
# Solution from: https://www.youtube.com/watch?v=tZAa_jJ3SwQ
from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0

        for i in range(len(nums)):
            if i > max_index:
                return False
            max_index = max(max_index, i + nums[i])

        return True