# https://www.geeksforgeeks.org/problems/subset-sums2234/1
class Solution:
    def subsetSums(self, arr):
        result = []
        curr_subset = []
        
        def dfs(index):
            if index == len(arr):
                result.append(sum(curr_subset))
                return
            
            # add current index
            curr_subset.append(arr[index])
            dfs(index + 1)
            
            # skip current index
            curr_subset.pop()
            dfs(index + 1)
        
        dfs(0)
        return result