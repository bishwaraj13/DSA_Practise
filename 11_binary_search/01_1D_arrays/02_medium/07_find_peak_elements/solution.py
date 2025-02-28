# https://leetcode.com/problems/find-peak-element/description/
from typing import *

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # edge case: if single element
        if n == 1:
            return 0

        # to keep code clean, we will already check 0th index and (n-1)th index
        if nums[0] > nums[1]:
            return 0

        if nums[n-1] > nums[n - 2]:
            return n-1

        low = 1
        high = n-2

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1]:
                # its in the left subset
                # then the peak is in right
                low = mid + 1
            else:
                # its in the right subset
                # and the peak is in left
                high = mid - 1
