# the test did not pass, but this is how we should generally do.. using left + right
class Solution:
    def perfectSum(self, arr, target):
        def dfs(index, curr_sum):
            if curr_sum == target:
                return 1
            
            if index >= len(arr) or curr_sum > target:
                return 0
            
            # include current element
            left = dfs(index+1, curr_sum + arr[index])
            
            # dont include curr element
            right = dfs(index+1, curr_sum)
            
            return left + right
        
        return dfs(0, 0)