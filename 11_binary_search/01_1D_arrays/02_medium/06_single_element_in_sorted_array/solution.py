# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
from typing import *

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        # edge case: if single element
        if n == 1:
            return nums[0]

        # to keep code clean, we will already check 0th index and (n-1)th index
        if nums[0] != nums[1]:
            return nums[0]

        if nums[n-1] != nums[n - 2]:
            return nums[n-1]

        low = 1
        high = n-2

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            
            # if odd index, and prev elem is same as curr,
            # it means mid is at left subset
            # OR
            # if even index, and next elem is same as curr,
            # that too means mid is on left subset
            if (
                (mid % 2 == 1 and nums[mid-1] == nums[mid]) or 
                (mid % 2 == 0 and nums[mid+1] == nums[mid])
            ):
                # eliminate the left half
                low = mid + 1
            else:
                # mid is in right subset,
                # so we eliminate the right half
                high = mid - 1
