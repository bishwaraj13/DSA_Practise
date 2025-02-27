# https://www.naukri.com/code360/problems/count-subsets-with-sum-k_3952532
from typing import List

def findWays(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [[-1 for j in range(k+1)] for i in range(n)]

    def dfs(index, currSum):
        if currSum == 0:
            return 1
        if index == 0:
            if currSum == arr[index]:
                return 1
            return 0
        
        if dp[index][currSum] != -1:
            return dp[index][currSum]
            
        notPick = dfs(index-1, currSum)
        pick = 0

        if arr[index] <= currSum:
            pick = dfs(index-1, currSum-arr[index])

        dp[index][currSum] = pick + notPick

        return dp[index][currSum]

    MOD = int(1e9 + 7)
    return dfs(len(arr)-1, k) % MOD

print(findWays([1,1,4,5], 5))