# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/
class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        
        # Generate all possible substrings
        for i in range(len(s)):
            # Initialize a frequency counter for each starting position
            char_freq = {}
            
            for j in range(i, len(s)):
                # Update the frequency of the current character
                char = s[j]
                char_freq[char] = char_freq.get(char, 0) + 1
                
                # Calculate beauty (max frequency - min frequency)
                if len(char_freq) > 1:  # Need at least 2 different characters
                    max_freq = max(char_freq.values())
                    min_freq = min(char_freq.values())
                    beauty = max_freq - min_freq
                    total_beauty += beauty
        
        return total_beauty