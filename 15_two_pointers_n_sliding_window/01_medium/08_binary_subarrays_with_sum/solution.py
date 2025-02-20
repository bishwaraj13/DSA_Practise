# https://leetcode.com/problems/binary-subarrays-with-sum/description/
from typing import *

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
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
                sum_total += nums[r]

                while sum_total > g:
                    sum_total -= nums[l]
                    l += 1

                count = count + (r-l+1)
                r += 1
            return count

            
        # compute subarrays whose sum are <= goal
        num1 = compute_subarrays_with_less_or_equal_goal(goal)

        # computer subarrays whose sum are <= goal-1
        num2 = compute_subarrays_with_less_or_equal_goal(goal-1)

        return num1 - num2