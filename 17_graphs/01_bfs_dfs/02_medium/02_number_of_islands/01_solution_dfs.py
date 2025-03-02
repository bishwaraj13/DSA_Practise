# https://leetcode.com/problems/number-of-islands/
from typing import *

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i > ROWS-1 or j > COLS-1 or \
            grid[i][j] == 0 or visit[i][j] == 1:
                return

            if grid[i][j] == 1:
                visit[i][j] = 1
                dfs(i-1, j)
                dfs(i, j-1)
                dfs(i+1, j)
                dfs(i, j+1)

        ROWS, COLS = len(grid), len(grid[0])
        visit = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        total_islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if visit[i][j] == 1:
                    continue
                elif visit[i][j] == 0 and grid[i][j] == 1:
                    dfs(i, j)
                    total_islands += 1
                    
        return total_islands
