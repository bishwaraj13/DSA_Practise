# https://leetcode.com/problems/rotate-array/
# this is tricky solution to come up with
# it involves reversing the array 3 times
# first reverse the entire array
# then reverse the first k elements
# then reverse the remaining elements
# this is an efficient solution
# Time complexity: O(n)
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # reverse entire array
        reverse(nums, 0, len(nums) - 1)

        # reverse first k elements
        reverse(nums, 0, k-1)

        # reverse remaining elements
        reverse(nums, k, len(nums) - 1)