from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] != nums[right]:
                # value in right pointer is different
                # means we found another unique element.

                # so, we move the new unique element to next index
                left += 1
                nums[left] = nums[right]
            right += 1
        # left index is from 0, 
        # so to get unique element list, we add 1
        return left + 1