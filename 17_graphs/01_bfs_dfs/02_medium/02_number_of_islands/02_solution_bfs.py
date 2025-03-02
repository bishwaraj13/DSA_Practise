# https://leetcode.com/problems/number-of-islands/
from typing import *

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            queue = [(i, j)]
            visit[i][j] = 1
            
            while queue:
                row, col = queue.pop(0)
                
                # Check all 4 directions
                directions = [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]
                
                for r, c in directions:
                    if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or \
                    grid[r][c] == 0 or visit[r][c] == 1:
                        continue
                    
                    if grid[r][c] == 1:
                        visit[r][c] = 1
                        queue.append((r, c))

        ROWS, COLS = len(grid), len(grid[0])
        visit = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        total_islands = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if visit[i][j] == 1:
                    continue
                elif visit[i][j] == 0 and grid[i][j] == 1:
                    bfs(i, j)
                    total_islands += 1
                    
        return total_islands