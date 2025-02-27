# https://www.naukri.com/code360/problems/count-subsets-with-sum-k_3952532
from typing import *

def findWays(arr: List[int], k: int) -> int:
    def dfs(index, currSum):
        if currSum == 0:
            return 1
        
        if index == 0:
            if arr[0] == currSum:
                return 1
 
            return 0
            
        notPick = dfs(index-1, currSum)
        pick = 0

        if arr[index] <= currSum:
            pick = dfs(index-1, currSum-arr[index])

        return pick + notPick

    MOD = int(1e9 + 7)
    return dfs(len(arr)-1, k) % MOD

print(findWays([1,1,4,5], 5))