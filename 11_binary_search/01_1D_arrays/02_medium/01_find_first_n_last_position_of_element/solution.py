# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import *

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_index = self.lowerBound(nums, target)
        upper_index = self.upperBound(nums, target)

        if lower_index == len(nums) or nums[lower_index] != target:
            return [-1, -1]

        return [lower_index, upper_index-1]

    def lowerBound(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                ans = mid
                # go more left to see if there are other element
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def upperBound(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans