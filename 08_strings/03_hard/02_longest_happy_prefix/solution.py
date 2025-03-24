# https://leetcode.com/problems/longest-happy-prefix/
class Solution:
    def longestPrefix(self, s: str) -> str:
        # Edge cases
        if not s or len(s) <= 1:
            return ""
        
        prefix_hash = 0
        suffix_hash = 0
        base = 29
        mod = 10**9 + 7
        longest_match_idx = 0
        
        # Computing power for suffix calculation
        power = 1
        
        # Iterate through the string (excluding the entire string itself)
        for i in range(len(s) - 1):
            ch_val = ord(s[i]) - ord('a') + 1
            last_ch_val = ord(s[len(s) - 1 - i]) - ord('a') + 1
            
            # Update the prefix hash (left to right)
            # Similar to computing: "a" -> "ab" -> "abc"
            prefix_hash = (prefix_hash * base + ch_val) % mod
            
            # Update the suffix hash (right to left)
            # Similar to computing: "c" -> "bc" -> "abc"
            suffix_hash = (suffix_hash + last_ch_val * power) % mod
            power = (power * base) % mod
            
            # If hashes match, we found a potential happy prefix
            if prefix_hash == suffix_hash:
                longest_match_idx = i + 1  # +1 because i is 0-indexed
        
        # Return the longest prefix found
        return s[:longest_match_idx]