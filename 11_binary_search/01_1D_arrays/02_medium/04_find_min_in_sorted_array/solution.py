# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
import sys
from typing import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = sys.maxsize
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # check if left half is sorted
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                # eliminate left half and move to UNSORTED half
                low = mid + 1
            # this means right half is sorted
            else:
                ans = min(ans, nums[mid])
                # eliminate right half and move to UNSORTED half
                high = mid - 1

        return ans