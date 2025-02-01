# https://leetcode.com/problems/sort-colors/
# solved using bucket sort
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]

        for num in nums:
            if num == 0:
                buckets[0] += 1
            elif num == 1:
                buckets[1] += 1
            else:
                buckets[2] += 1

        index = 0
        for i in range(len(buckets)):
            count = buckets[i]

            while index < len(nums) and count > 0:
                nums[index] = i
                index += 1
                count -= 1