# https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1
class Solution:
    def perfectSum(self, arr, target):
        def dfs(index, curr_sum):
            if index == len(arr):
                if curr_sum == target:
                    return 1
                else:
                    return 0
            
            # include current element
            left = dfs(index+1, curr_sum + arr[index])
            
            # dont include curr element
            right = dfs(index+1, curr_sum)
            
            return left + right
        
        return dfs(0, 0)
    
print(Solution().perfectSum([0, 10, 0], 0))