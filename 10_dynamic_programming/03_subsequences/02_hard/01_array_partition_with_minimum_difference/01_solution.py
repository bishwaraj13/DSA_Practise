# https://www.naukri.com/code360/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494
# This problem and subsetSum problem is very similar if you compare the code
from typing import List

def minSubsetSumDifference(arr: List[int], n: int) -> int:
    # Calculate total sum of array
    total_sum = sum(arr)
    
    # Recursive helper function
    def subset_diff(index, current_sum):
        # Base case: if we've processed all elements
        if index == 0:
            # Calculate other subset sum and find difference
            other_sum = total_sum - current_sum
            return abs(other_sum - current_sum)
        
        # Two choices for each element:
        # 1. Include in first subset
        include = subset_diff(index - 1, current_sum + arr[index - 1])
        
        # 2. Exclude (implicitly include in second subset)
        exclude = subset_diff(index - 1, current_sum)
        
        # Return minimum of both choices
        return min(include, exclude)
    
    # Start recursion from last element with current_sum = 0
    return subset_diff(n, 0)