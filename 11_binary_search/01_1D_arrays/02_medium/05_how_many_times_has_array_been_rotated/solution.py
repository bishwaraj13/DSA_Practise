# https://www.geeksforgeeks.org/problems/rotation4723/1
import sys

class Solution:
    def findKRotation(self, arr):
        ans = sys.maxsize
        index = -1
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # check if left half is sorted
            if arr[low] <= arr[mid]:
                if arr[low] < ans:
                    ans = arr[low]
                    index = low
                # eliminate left half and move to UNSORTED half
                low = mid + 1
            # this means right half is sorted
            else:
                if arr[mid] < ans:
                    ans = arr[mid]
                    index = mid

                # eliminate right half and move to UNSORTED half
                high = mid - 1

        return index