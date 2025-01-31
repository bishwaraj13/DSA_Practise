# https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k
# That question is not available for free on Leetcode
# The following code is right, if the array contains only positive numbers.
class Solution:
    def longestSubarray(self, arr, k):
        print(f"\nInput Array: {arr}, Target Sum: {k}")  # Debug input values
        
        if not arr:
            print("Empty array detected, returning 0")
            return 0
            
        l = r = 0
        longest_subarray = 0
        sum_tracker = arr[l]
        
        print(f"Initial window: l={l}, r={r}, sum={sum_tracker}")  # Debug initial state
        
        while r+1 < len(arr):
            print(f"\n--- Current Window State ---")
            print(f"Window indices: l={l}, r={r}")
            print(f"Current window: {arr[l:r+1]}")
            print(f"Current sum: {sum_tracker}")
            
            if sum_tracker == k:
                longest_subarray = max(longest_subarray, r - l + 1)
                print(f"Found valid window! Length = {r-l+1}, Longest so far = {longest_subarray}")
                
            if sum_tracker < k and r+1 < len(arr):
                print(f"Sum ({sum_tracker}) < k ({k}), expanding window right")
                r += 1
                sum_tracker += arr[r]
                print(f"Added {arr[r]} at index {r}, new sum = {sum_tracker}")
            else: 
                print(f"Sum ({sum_tracker}) >= k ({k}), shrinking window from left")
                while sum_tracker >= k and l < r:
                    print(f"Removing {arr[l]} at index {l}")
                    sum_tracker -= arr[l]
                    l += 1
                    print(f"New window after shrinking: l={l}, r={r}, sum={sum_tracker}")
        
        print(f"\nFinal result: {longest_subarray}")
        return longest_subarray
    
solution = Solution().longestSubarray([10, 5, 2, 7, 1, -10], 15)

