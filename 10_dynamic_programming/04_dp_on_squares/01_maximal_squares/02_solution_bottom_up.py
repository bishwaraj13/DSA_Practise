# https://leetcode.com/problems/maximal-square/
from typing import *

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        ROWS, COLS = len(matrix), len(matrix[0])
        # added extra row and column for padding
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        max_side = 0
        
        # Bottom-up DP approach
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if matrix[r][c] == "1":
                    # Take the minimum of right, down, and diagonal values + 1
                    dp[r][c] = 1 + min(dp[r+1][c], dp[r][c+1], dp[r+1][c+1])
                    max_side = max(max_side, dp[r][c])
        
        return max_side ** 2