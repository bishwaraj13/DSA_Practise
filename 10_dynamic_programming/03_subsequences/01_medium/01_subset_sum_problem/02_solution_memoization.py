# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
class Solution:
    def isSubsetSum (self, arr, target):
        dp = [[None for j in range(target + 1)] for i in range(len(arr))]

        # t is target
        def dfs(i, t):
            # base condition 1
            if t == 0:
                return True
              
            # base condition 2  
            if i == 0:
                if t == arr[i]:
                    return True
                else:
                    return False
                    
            if dp[i][t] is not None:
                return dp[i][t]
            
            not_take = dfs(i-1, t)
            take = False
            
            if t >= arr[i]:
                take = dfs(i-1, t-arr[i])
                
            
            dp[i][t] = take or not_take
            return dp[i][t]
            
        return dfs(len(arr)-1, target)
    
print(Solution().isSubsetSum([3,34,4,12,5,2], 9))