# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated
def check_sorted_rotated(nums):
    n = len(nums)
    # Count irregularities (where next number is smaller than current)
    irregularities = 0
    
    # Check between adjacent elements
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            irregularities += 1
    
    # Check between last and first element
    # (already covered in the loop above using modulo)
    
    # If array is sorted and rotated, we should have exactly one irregularity
    # If array is just sorted (no rotation), we should have one irregularity at the end (last element is smaller than first element)
    print(f"irregularities: {irregularities}")
    return irregularities <= 1

print(check_sorted_rotated([3, 4, 5, 1, 2]))  # True
