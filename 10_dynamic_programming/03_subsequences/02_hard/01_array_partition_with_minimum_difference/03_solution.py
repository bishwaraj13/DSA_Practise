# https://www.naukri.com/code360/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494
# this problem uses ditto tabulation solution from subset sum problem
# Only at last we have one extra loop
from typing import List

def minSubsetSumDifference(arr: List[int], n: int) -> int:
    totSum = sum(arr)

    # lets make a dp table for target sum of totSum
    # this is based on subset sum problem

    # step 1: initialize dp cache of (n x  totSum+1)
    dp = [[None for j in range(totSum+1)] for i in range(n)]

    # step 2 [Base Condition 1]: In dp, for target as 0, no matter what i is, the value will be True
    # because if target is 0, means we always can return null subset
    t = 0
    for i in range(n):
        dp[i][t] = True

    # step 3 [Base Condition 2]: while memoization, we traverse from (n-1) to 0,
    # if last element (i.e, index 0) is equal to target
    # that means its True 
    i = 0
    t = arr[i]

    if arr[i] <= totSum:
        dp[0][t] = True

    # step 3: Iterate i from 1 to n-1 and fill in details
    for i in range(1, n):
        for t in range(totSum+1):
            not_take = dp[i-1][t]

            take = False
            if t >= arr[i]:
                take = dp[i-1][t-arr[i]]

            dp[i][t] = take or not_take

    # now dp is a 2d array whose last row tells if any value from 0 to totSum is possible
    mini = 1e9

    # this loop will give same result if you do totSum/2
    for s1 in range(0, totSum):
        if dp[n-1][s1] == True:
            mini = min(mini, abs((totSum-s1) - s1))

    return mini
    
print(minSubsetSumDifference([3, 1, 5, 2, 8], 5))