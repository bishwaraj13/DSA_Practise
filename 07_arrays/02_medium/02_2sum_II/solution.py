# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1527254930/
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            val = numbers[l] + numbers[r]

            if val == target:
                return [l+1, r+1]
            elif val < target:
                l += 1
            else:
                r -= 1
