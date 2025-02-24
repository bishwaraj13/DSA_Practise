# https://leetcode.com/problems/minimum-path-sum/description/
from typing import *

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i == 0 and j == 0:
                return grid[0][0]

            if i < 0 or j < 0:
                return float("inf")

            up = grid[i][j] + dfs(i-1, j)
            left = grid[i][j] + dfs(i, j-1)

        
            return min(up, left)

        return dfs(len(grid)-1, len(grid[0])-1)