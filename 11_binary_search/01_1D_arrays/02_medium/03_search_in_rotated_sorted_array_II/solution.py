# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            m = (low + high) // 2

            if nums[m] == target:
                return True

            # *******Add this if clause*******
            if nums[low] == nums[m] and nums[m] == nums[high]:
                # shrink array
                low += 1
                high -= 1
                continue

            # check if left half is sorted
            if nums[low] <= nums[m]:
                if nums[low] <= target and target <= nums[m]:
                    high = m - 1
                else:
                    low = m + 1
            # this means right half is sorted
            else:
                if nums[m] < target and target <= nums[high]:
                    low = m + 1
                else:
                    high = m - 1

        return False