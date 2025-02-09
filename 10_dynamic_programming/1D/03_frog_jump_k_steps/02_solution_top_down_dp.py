# https://www.geeksforgeeks.org/problems/minimal-cost/1
class Solution:
    def minimizeCost(self, k, arr):
        dp_cache = [float("inf")] * len(arr)

        def dfs(n):
            if n == 0:
                return 0
            
            if dp_cache[n] != float("inf"):
                return dp_cache[n]
                
            k_min_costs =[float("inf")] * k
            
            for i in range(0, k):
                # because steps should not be from 0 to k-1,
                # but 1 to k
                steps = i+1
                if n-steps >= 0:
                    if dp_cache[n-steps] == float("inf"):
                        dp_cache[n-steps] = dfs(n-steps)
                    k_min_costs[i] = dp_cache[n-steps] + abs(arr[n] - arr[n-steps])

                dp_cache[n] = min(k_min_costs)
            return dp_cache[n]
            
        return dfs(len(arr)-1)