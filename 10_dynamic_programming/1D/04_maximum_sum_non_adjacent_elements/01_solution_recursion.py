# https://www.naukri.com/code360/problems/maximum-sum-of-non-adjacent-elements_843261
def maximumNonAdjacentSum(nums):
    def dfs(index):
        if index == 0:
            return nums[0]

        if index < 0:
            return 0

        # include current element
        left = nums[index] + dfs(index-2)

        # dont include current element
        right = dfs(index-1)

        return max(left, right)

    return dfs(len(nums)-1)