# https://leetcode.com/problems/count-number-of-nice-subarrays/
from typing import *

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        odd_count = 0
        count = 0
        temp = 0

        while r < len(nums):
            # Count odd numbers in current window
            if nums[r] % 2 != 0:
                odd_count += 1
                temp = 0

            # Shrink window if too many odd numbers
            while odd_count > k:
                if nums[l] % 2 != 0:
                    odd_count -= 1
                l += 1

            # Count subarrays when we have exactly k odd numbers
            while odd_count == k:
                temp += 1
                if nums[l] % 2 != 0:
                    odd_count -= 1
                l += 1

            count += temp
            r += 1

        return count