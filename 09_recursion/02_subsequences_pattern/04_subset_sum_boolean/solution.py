# https://www.naukri.com/code360/problems/subset-sum_630213
# return true is subset has sum = k.. meaning dont execute other subset if you found one
from typing import *

def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    # Write your code here.
    curr_subset = []

    def dfs(index, curr_sum):
        if curr_sum == k:
            return True

        if index >= n or curr_sum > k:
            return False

        # include current element
        curr_subset.append(a[index])

        if dfs(index+1, curr_sum + a[index]):
            return True

        # dont include current element
        curr_subset.pop()

        if dfs(index+1, curr_sum):
            return True
        
        return False

    return dfs(0, 0)
