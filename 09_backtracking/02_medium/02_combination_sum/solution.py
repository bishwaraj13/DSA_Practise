# https://leetcode.com/problems/combination-sum/
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr_subset = []

        def dfs(index, curr_sum):
            if curr_sum == target:
                result.append(curr_subset.copy())
                return

            if index >= len(candidates) or curr_sum > target:
                return

            # include current element
            curr_subset.append(candidates[index])
            dfs(index, curr_sum + candidates[index])

            # dont include current element
            curr_subset.pop()
            dfs(index+1, curr_sum)

        dfs(0, 0)

        return result