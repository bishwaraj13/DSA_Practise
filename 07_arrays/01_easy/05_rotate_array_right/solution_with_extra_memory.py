# https://leetcode.com/problems/rotate-array/
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()

        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = temp[i]