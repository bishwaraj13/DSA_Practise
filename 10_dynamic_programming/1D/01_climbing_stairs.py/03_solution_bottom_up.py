# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        # step 1 is index 0, step 2 is index 1, step 3 is index 2, ..
        dp_cache = [-1] * n
        dp_cache[0] = 1

        if n > 1:
            dp_cache[1] = 2

        for i in range(len(dp_cache)):
            if i <= 1:
                continue
            dp_cache[i] = dp_cache[i-1] + dp_cache[i-2]

        return dp_cache[n-1]