# https://leetcode.com/problems/move-zeroes/
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 

        n = len(nums)
        left = 0

        while left < n:
            while (left < n) and nums[left] != 0:
                left += 1
            
            right = left + 1

            while (right < n) and (nums[right] == 0):
                right += 1

            if right >= n:
                break

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        

        