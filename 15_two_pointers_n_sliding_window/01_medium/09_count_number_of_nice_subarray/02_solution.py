# https://leetcode.com/problems/count-number-of-nice-subarrays/
# This is a clever solution done as a copy of binary_subarrays_with_sum
from typing import *

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def compute_subarrays_with_less_or_equal_goal(g):
            if g < 0:
                return 0

            l = 0
            r = 0
            sum_total = 0
            count = 0

            # algorithm to track count of subarrays whose sum <= goal
            # but note that the question asked for sum == goal
            while r < len(nums):
                sum_total += (nums[r] % 2)

                while sum_total > g:
                    sum_total -= (nums[l] % 2)
                    l += 1

                count = count + (r-l+1)
                r += 1
            return count

        # compute subarrays whose sum are <= goal
        num1 = compute_subarrays_with_less_or_equal_goal(k)

        # computer subarrays whose sum are <= goal-1
        num2 = compute_subarrays_with_less_or_equal_goal(k-1)

        return num1 - num2