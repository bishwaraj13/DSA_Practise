# https://leetcode.com/problems/max-consecutive-ones-iii/description/
# This is optimized solution compared to previous one.
# Here we removed inner while loop
from typing import *

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        zeros = 0
        maxlen = 0

        while r < len(nums):
            if nums[r] == 0:
                zeros += 1

            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            # because we removed inner while loop,
            # there is no guarantee that zeros dont exceed k.
            # So, before we update maxlen, let's check
            if zeros <= k:
                maxlen = max(maxlen, r-l+1)
            r += 1

        return maxlen