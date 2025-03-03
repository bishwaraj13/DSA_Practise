# https://leetcode.com/problems/number-of-enclaves/
from typing import *

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        # DFS to mark all land cells connected to the boundary
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1):
                return
            
            # Mark this land cell as visited
            grid[r][c] = -1  # Temporary marker
            
            # Check all four directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # Start DFS from all boundary cells that are land
        for r in range(rows):
            if grid[r][0] == 1:
                dfs(r, 0)       # Left boundary
            if grid[r][cols-1] == 1:
                dfs(r, cols-1)  # Right boundary
        
        for c in range(cols):
            if grid[0][c] == 1:
                dfs(0, c)       # Top boundary
            if grid[rows-1][c] == 1:
                dfs(rows-1, c)  # Bottom boundary
        
        # Count the number of land cells that cannot reach the boundary
        enclave_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    enclave_count += 1
                elif grid[r][c] == -1:
                    # Restore the original grid (optional)
                    grid[r][c] = 1
        
        return enclave_count