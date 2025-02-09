# https://www.naukri.com/code360/problems/maximum-sum-of-non-adjacent-elements_843261
def maximumNonAdjacentSum(nums):
    curr_subset = []
    max_sum = float("-inf")

    def dfs(index):
        nonlocal max_sum
        if index >= len(nums):
            max_sum = max(max_sum, sum(curr_subset))
            return max_sum

        # pick current element
        curr_subset.append(nums[index])
        left = dfs(index+2)

        # dont pick current element
        curr_subset.pop()
        right = dfs(index+1)

        return max(left, right)

    if not nums:
        return 0
    
    return dfs(0)