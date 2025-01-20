# https://leetcode.com/problems/rotate-array/
# inefficient solution: O(k * n)
# inefficient because we are shifting the elements one by one and if k is large, it will take a lot of time
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        while k > 0:
            last_element = nums[n-1]

            # shift all the element to right
            for i in range(n-2, -1, -1):
                nums[i+1] = nums[i]

            # move last element to 0th index
            nums[0] = last_element
            k -= 1
        