# https://www.naukri.com/code360/problems/maximum-sum-of-non-adjacent-elements_843261
def maximumNonAdjacentSum(nums):
    if not nums:
        return 0
    
    dp_cache = [float("-inf")] * len(nums)
    dp_cache[0] = nums[0]

    for i in range(1, len(nums)):
        left = float("-inf")
        right = float("-inf")

        if i-2 >= 0:
            left = nums[i] + dp_cache[i-2]
        else:
            left = nums[i]
        
        if i-1 >= 0:
            right = dp_cache[i-1]

        dp_cache[i] =  max(left, right)

    return dp_cache[len(nums)-1]