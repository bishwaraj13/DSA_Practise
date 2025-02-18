# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        l = 0
        r = 0
        hashmap = {}

        while (r < len(s)):
            while hashmap.get(s[r], 0):
                hashmap[s[l]] = 0
                l += 1

            hashmap[s[r]] = 1
            longest_substring = max(r-l+1, longest_substring)
            r += 1

        return longest_substring