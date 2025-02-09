# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(index):
            if index <= 2:
                return index

            left = dfs(index-1)
            right = dfs(index-2)

            return left+right

        return dfs(n)