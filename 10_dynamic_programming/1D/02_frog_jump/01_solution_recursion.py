# https://www.geeksforgeeks.org/problems/geek-jump/1
class Solution:
    def minCost(self, height):
        def dfs(index):
            if index == 0:
                return 0
                
            left = float("inf")
            if index-1 >= 0:
                left = dfs(index-1) + abs(height[index]-height[index-1])
                
            right = float("inf")
            
            if index-2 >= 0:
                right = dfs(index-2) + abs(height[index]-height[index-2])
            
            return min(left, right)
            
        return dfs(len(height)-1)