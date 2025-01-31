# https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k
# This problems is solved using prefix sum technique.
class Solution:
    def longestSubarray(self, arr, k):
        if not arr:
            return 0
            
        prefix_sum = {0: -1}
        longest_sum = 0
        current_sum = 0
        
        for index, num in enumerate(arr):
            current_sum += num
            
            if (current_sum - k) in prefix_sum:
                longest_sum = max(longest_sum, index - prefix_sum[current_sum - k])
                
            # update dictionary only if current_sum not present.
            # this ensures that only leftmost index is considered
            if current_sum not in prefix_sum:
                prefix_sum[current_sum] = index
                
        return longest_sum