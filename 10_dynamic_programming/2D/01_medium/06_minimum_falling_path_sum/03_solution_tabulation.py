# https://leetcode.com/problems/minimum-falling-path-sum/
from typing import *

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float("inf") for j in range(n)] for i in range(n)]

        # base condition
        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(n):
                straight = matrix[i][j] + dp[i-1][j]

                left_diagonal = float("inf")
                right_diagonal = float("inf")
                if j-1 >= 0:
                    left_diagonal = matrix[i][j] + dp[i-1][j-1]
                if j+1 <= n-1:
                    right_diagonal = matrix[i][j] + dp[i-1][j+1]

                dp[i][j] = min(straight, left_diagonal, right_diagonal)

        return min(dp[n-1][j] for j in range(n))