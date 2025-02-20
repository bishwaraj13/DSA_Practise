# https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        hashmap = [0] * 26
        l = 0
        r = 0
        longest = 0

        while r < len(s):
            hashmap[ord(s[r]) - ord('A')] += 1
            maxf = max(hashmap)

            if (r-l+1) - maxf > k:
                hashmap[ord(s[l]) - ord('A')] -= 1
                l += 1

            if (r-l+1) - maxf <= k:
                # its a valid segment
                longest = max(r-l+1, longest)

            r += 1

        return longest