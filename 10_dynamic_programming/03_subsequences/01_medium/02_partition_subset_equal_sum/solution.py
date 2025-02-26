# https://leetcode.com/problems/partition-equal-subset-sum/
# this solution is entirely built on 01_subset_sum_problem
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # if total_sum is odd, this means two subsets cant have same sum
        if total_sum % 2 != 0:
            return False

        # now we need to find if there is one subset whose sum is total_sum / 2
        # If there is one subset, it means its possible there are two subsets with sum total_sum/2
        # because they would sum to become total_sum
        return self.isSubsetSum(nums, total_sum//2)

    def isSubsetSum (self, arr, target):
        n = len(arr)
        dp = [[False for j in range(target + 1)] for i in range(n)]

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