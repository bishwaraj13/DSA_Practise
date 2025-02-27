# https://leetcode.com/problems/search-insert-position/
from typing import *

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        l = 0
        h = n - 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                ans = mid
                h = mid - 1
            else:
                ans = mid + 1
                l = mid + 1

        return ans