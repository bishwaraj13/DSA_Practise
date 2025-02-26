# https://www.geeksforgeeks.org/problems/minimal-cost/1
class Solution:
    def minimizeCost(self, k, arr):
        def dfs(n):
            if n == 0:
                return 0
                
            k_min_costs =[float("inf")] * k
            
            for i in range(0, k):
                # because steps should not be from 0 to k-1,
                # but 1 to k
                steps = i+1
                if n-steps >= 0:
                    k_min_costs[i] = dfs(n-steps) + abs(arr[n] - arr[n-steps])
                    
            return min(k_min_costs)
            
        return dfs(len(arr)-1)
    
print(Solution().minimizeCost(3, [10, 30, 40, 50, 20]))