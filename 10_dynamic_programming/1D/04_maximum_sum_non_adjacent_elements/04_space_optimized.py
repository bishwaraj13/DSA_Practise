# https://www.naukri.com/code360/problems/maximum-sum-of-non-adjacent-elements_843261
def maximumNonAdjacentSum(nums):
    if not nums:
        return 0
    
    prev = nums[0]
    prev_prev = float("-inf")
    curr = prev

    for i in range(1, len(nums)):
        left = float("-inf")
        right = float("-inf")

        if prev_prev != float("-inf"):
            left = nums[i] + prev_prev
        else:
            left = nums[i]

        right = prev
        
        curr = max(left, right)
        prev_prev = prev
        prev = curr

    return curr