# https://leetcode.com/problems/surrounded-regions/
from typing import *

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        # Step 1: Mark 'O's connected to the boundary with a temporary marker
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O'):
                return
            
            # Mark this cell as visited
            board[r][c] = 'T'  # Temporary marker
            
            # Check all four directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # Start DFS from all boundary cells
        for r in range(rows):
            dfs(r, 0)           # Left boundary
            dfs(r, cols-1)      # Right boundary
        
        for c in range(cols):
            dfs(0, c)           # Top boundary
            dfs(rows-1, c)      # Bottom boundary
        
        # Step 2: Capture surrounded regions by flipping 'O's to 'X's
        # and restore temporary markers back to 'O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Capture surrounded 'O's
                elif board[r][c] == 'T':
                    board[r][c] = 'O'  # Restore boundary-connected 'O's
        