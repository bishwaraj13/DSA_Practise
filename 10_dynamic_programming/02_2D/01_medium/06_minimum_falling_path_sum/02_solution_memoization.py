# https://leetcode.com/problems/minimum-falling-path-sum/
from typing import *

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float("inf") for j in range(n)] for i in range(n)]

        def dfs(i, j):
            if j < 0 or j >= n:
                return float("inf")

            if i == 0:
                return matrix[0][j]
            
            if dp[i][j] != float("inf"):
                return dp[i][j]

            straight = matrix[i][j] + dfs(i-1, j)
            left_diagonal = matrix[i][j] + dfs(i-1, j-1)
            right_diagonal = matrix[i][j] + dfs(i-1, j+1)

            dp[i][j] = min(straight, left_diagonal, right_diagonal)

            return dp[i][j]

        # Check all possible ending positions in the last row
        return min(dfs(n-1, j) for j in range(n))