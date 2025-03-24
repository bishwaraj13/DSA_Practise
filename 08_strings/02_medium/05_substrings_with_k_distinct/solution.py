# https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1
class Solution:
    def countSubstr(self, s, k):
        # Helper function to count substrings with at most k distinct characters
        def atMostK(s, k):
            if k == 0:
                return 0
                
            count = 0
            char_freq = {}
            left = 0
            
            for right in range(len(s)):
                # Add current character to frequency map
                char_freq[s[right]] = char_freq.get(s[right], 0) + 1
                
                # Shrink window while we have more than k distinct characters
                while len(char_freq) > k:
                    char_freq[s[left]] -= 1
                    if char_freq[s[left]] == 0:
                        del char_freq[s[left]]
                    left += 1
                
                # For each valid window, add the number of substrings ending at right
                count += right - left + 1
                
            return count
        
        # Count of substrings with exactly k distinct characters
        return atMostK(s, k) - atMostK(s, k-1)