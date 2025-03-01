# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2

        if n1 > n2:
            # we keep shorter array on the left to keep search space smaller
            return self.findMedianSortedArrays(nums2, nums1)

        # edge cases
        if not n1 and n2:
            return self.median_of_array(nums2, n2)

        if n1 and not n2:
            return self.median_of_array(nums1, n1)

        if not n1 and not n2:
            return 0

        # search space is how many elements from nums1 is considered for left subarray
        # of the presumed merged array
        low = 0
        high = n1

        # total elements in left subarray of presumed merged array
        leftSubarraySize = (n1 + n2 + 1) // 2

        while low <= high:
            # mid1 - 1 is the elements from nums1 for l1
            mid1 = (low + high) // 2
            # mid2 - 1 is the elements from nums2 for l2
            mid2 = leftSubarraySize - mid1

            # l1, l2 are largest element of subarray taken from nums1 and nums2,
            # for left half of presumed merged array
            l1 = float("-inf")
            l2 = float("-inf")

            # r1, r2 are largest element of subaray taken from nums1 and nums2.
            # for right half of presumed merged subarray
            # mid1 points to r1, and mid2 points to r2
            r1 = float("inf")
            r2 = float("inf")

            if mid1 < n1:
                r1 = nums1[mid1]

            if mid2 < n2:
                r2 = nums2[mid2]

            if mid1-1 >= 0:
                l1 = nums1[mid1-1]

            if mid2-1 >= 0:
                l2 = nums2[mid2-1]

            if l1 <= r2 and l2 <= r1:
                if n % 2 != 0:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2

            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1

        return 0

    def median_of_array(self, arr, n):
        if n % 2 != 0:
            return arr[n // 2]
        else:
            return (arr[n // 2] + arr[(n - 1) // 2]) / 2
