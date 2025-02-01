# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            second_num = target - num

            if second_num in hashmap:
                return [i, hashmap[second_num]]

            hashmap[num] = i