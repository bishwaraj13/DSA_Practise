# https://leetcode.com/problems/unique-paths/description/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_cache = [[-1 for j in range(n)] for i in range(m)]

        dp_cache[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                up = 0
                left = 0
                if i > 0:
                    up = dp_cache[i-1][j]
                if j > 0:
                    left = dp_cache[i][j-1]

                dp_cache[i][j] = up + left

        return dp_cache[m-1][n-1]