# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev_prev = 1
        prev = 2
        curr = -1

        for i in range(3, n+1):
            curr = prev + prev_prev
            prev_prev = prev
            prev = curr

        return curr
    
print(Solution().climbStairs(4))
