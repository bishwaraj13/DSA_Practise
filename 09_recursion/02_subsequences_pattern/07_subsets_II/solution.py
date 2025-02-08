# https://leetcode.com/problems/subsets-ii/
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        curr_subset = []

        def dfs(index):
            if index == len(nums):
                result.append(curr_subset.copy())
                return

            # take current element
            curr_subset.append(nums[index])
            dfs(index+1)

            # skip current element
            curr_subset.pop()

            # skip duplicate elements
            while index < len(nums) - 1 and nums[index] == nums[index+1]:
                index += 1
            dfs(index+1)

        dfs(0)

        return result