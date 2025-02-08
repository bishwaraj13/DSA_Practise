# https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1
class Solution:
    def perfectSum(self, arr, target):
        result = 0
        curr_subset = []
        
        def dfs(index, curr_sum):
            nonlocal result

            if index == len(arr):
                if curr_sum == target:
                    result += 1
                return
            
            # include current element
            curr_subset.append(arr[index])
            dfs(index+1, curr_sum + arr[index])
            
            # dont include curr element
            curr_subset.pop()
            dfs(index+1, curr_sum)
        
        dfs(0, 0)
        return result
    
print(Solution().perfectSum([0, 10, 0], 0))