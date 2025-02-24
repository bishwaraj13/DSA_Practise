# https://leetcode.com/problems/unique-paths-ii/
from typing import *

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(i, j):
            if i >= 0 and j >= 0 and obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1

            if i < 0 or j < 0:
                return 0

            up = dfs(i-1, j)
            left = dfs(i, j-1)

            return up + left

        return dfs(len(obstacleGrid)-1, len(obstacleGrid[0])-1)