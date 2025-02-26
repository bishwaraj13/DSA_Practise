# https://leetcode.com/problems/minimum-path-sum/description/
# note: tabulation can be done in very similar way like unique-paths-i
from typing import *

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
        def dfs(i, j):
            if i >= 0 and j >= 0 and dp[i][j] != -1:
                return dp[i][j]

            if i == 0 and j == 0:
                return grid[0][0]

            if i < 0 or j < 0:
                return float("inf")

            up = grid[i][j] + dfs(i-1, j)
            left = grid[i][j] + dfs(i, j-1)

            dp[i][j] = min(up, left)
            return dp[i][j]

        return dfs(len(grid)-1, len(grid[0])-1)
    