# https://www.naukri.com/code360/problems/maximum-sum-of-non-adjacent-elements_843261
def maximumNonAdjacentSum(nums):
    dp_cache = [float("-inf")] * len(nums)

    def dfs(index):
        if index == 0:
            return nums[0]

        if index < 0:
            return 0
        
        if dp_cache[index] != float("-inf"):
            return dp_cache[index]

        # include current element
        left = nums[index] + dfs(index-2)

        # dont include current element
        right = dfs(index-1)

        dp_cache[index] = max(left, right)

        return dp_cache[index]

    return dfs(len(nums)-1)