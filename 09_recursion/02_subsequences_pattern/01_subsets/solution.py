# https://leetcode.com/problems/subsets/
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index):
            if index >= len(nums):
                results.append(curr_subset.copy())
                return

            # dont consider current element
            dfs(index+1)

            # consider current element
            curr_subset.append(nums[index])
            dfs(index+1)

            # remove added element
            curr_subset.pop()
        
        results = []
        curr_subset = []
        dfs(0)

        return results