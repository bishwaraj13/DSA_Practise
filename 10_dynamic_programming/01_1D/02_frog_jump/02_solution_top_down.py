# https://www.geeksforgeeks.org/problems/geek-jump/1
class Solution:
    def minCost(self, height):
        dp_cache = [float("inf")] * len(height)

        def dfs(index):
            if index == 0:
                return 0
            
            if dp_cache[index] != float("inf"):
                return dp_cache[index]
                
            left = float("inf")
            if index-1 >= 0:
                if dp_cache[index-1] != float("inf"):
                    left = dp_cache[index-1] + abs(height[index]-height[index-1])
                else:
                    dp_cache[index-1] = dfs(index-1)
                    left = dp_cache[index-1] + abs(height[index]-height[index-1])

                
            right = float("inf")
            
            if index-2 >= 0:
                if dp_cache[index-2] != float("inf"):
                    right = dp_cache[index-2] + abs(height[index]-height[index-2])
                else:
                    dp_cache[index-2] = dfs(index-2)
                    right = dp_cache[index-2] + abs(height[index]-height[index-2])

            dp_cache[index] = min(left, right)    
            return dp_cache[index]
            
        return dfs(len(height)-1)