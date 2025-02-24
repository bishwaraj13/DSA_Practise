# https://leetcode.com/problems/unique-paths/description/
from typing import *

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp_cache = [[-1 for j in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]

        def dfs(i, j):
            if i >= 0 and j >= 0 and obstacleGrid[i][j] == 1:
                return 0
            
            if i == 0 and j == 0:
                return 1

            if i < 0 or j < 0:
                return 0
            
            if dp_cache[i][j] is not -1:
                return dp_cache[i][j]

            up = dfs(i-1, j)
            left = dfs(i, j-1)

            dp_cache[i][j] = up + left
            return dp_cache[i][j]

        return dfs(len(obstacleGrid)-1, len(obstacleGrid[0])-1)
