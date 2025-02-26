# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
class Solution:
    def isSubsetSum (self, arr, target):
        n = len(arr)
        dp = [[None for j in range(target + 1)] for i in range(n)]

        # base condition 1
        t = 0
        for i in range(n):
            dp[i][t] = True

        # base condition 2
        if arr[0] <= target:
            dp[0][arr[0]] = True

        for i in range(1, n):
            for t in range(1, target+1):
                not_take = dp[i-1][t]
                take = False
                
                if t >= arr[i]:
                    take = dp[i-1][t-arr[i]]

                dp[i][t] = take or not_take


        return dp[n-1][target]


        
