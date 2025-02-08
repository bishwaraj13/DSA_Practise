# https://leetcode.com/problems/combination-sum-ii/
# Best explanation: Neetcode's https://www.youtube.com/watch?v=FOyRpNUSFeA
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr_subset = []
        candidates.sort()

        def dfs(index, curr_sum):
            if curr_sum == target:
                result.append(curr_subset.copy())
                return

            if curr_sum > target or index >= len(candidates):
                return

            # include current candidate
            curr_subset.append(candidates[index])
            dfs(index+1, curr_sum + candidates[index])

            # skip current candidate
            curr_subset.pop()

            # keep on iterating till you have no duplicates
            while index < len(candidates) - 1 and candidates[index] == candidates[index+1]:
                index += 1

            dfs(index+1, curr_sum)

        dfs(0, 0)

        return result