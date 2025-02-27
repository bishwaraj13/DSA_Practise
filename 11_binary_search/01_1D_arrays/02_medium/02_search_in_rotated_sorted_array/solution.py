# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            m = (low + high) // 2

            if nums[m] == target:
                return m

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

        return -1
    
print(Solution().search([4,5,6,7,0,1,2], 0))