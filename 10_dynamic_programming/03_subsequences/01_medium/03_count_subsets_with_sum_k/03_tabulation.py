# https://www.naukri.com/code360/problems/count-subsets-with-sum-k_3952532
from typing import List

def findWays(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [[0 for j in range(k+1)] for i in range(n)]

    # base condition 1
    t = 0
    for i in range(n):
        dp[i][t] = 1

    # base condition 2
    t = arr[0]
    if arr[0] <= k:
        dp[0][t] = 1

    # edge case where sum is 0 and arr[0] is 0
    if k == 0 and arr[0] == 0:
        dp[0][0] = 2

    for i in range(1, n):
        for j in range(1, k+1):
            notPick = dp[i-1][j]

            pick = 0
            if arr[i] <= j:
                pick = dp[i-1][j-arr[i]]

            dp[i][j] = pick + notPick

    return dp[n-1][k]

print(findWays([1,1,4,5], 5))