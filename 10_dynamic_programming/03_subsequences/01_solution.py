# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
class Solution:
    def isSubsetSum (self, arr, target):
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
                    
            
            not_take = dfs(i-1, t)
            take = False
            
            if t >= arr[i]:
                take = dfs(i-1, t-arr[i])
                
            
            return take or not_take
            
        return dfs(len(arr)-1, target)