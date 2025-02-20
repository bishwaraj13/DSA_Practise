# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# Clever solution: https://www.youtube.com/watch?v=xtqN4qlgr8s
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        # Array to store the last seen position of characters 'a', 'b', 'c'
        # Initialize with -1 to indicate characters haven't been seen yet
        last_seen = [-1, -1, -1]

        # Iterate through each character in the string
        for i in range(len(s)):
            # Update the last seen position for current character
            # ord(s[i]) - ord('a') converts character to index (0 for 'a', 1 for 'b', 2 for 'c')
            last_seen[ord(s[i]) - ord('a')] = i

            # Check if we have seen all characters (a, b, c)
            if -1 not in last_seen:
                # If all characters are present:
                # 1. min(last_seen) gives the smallest index position where we have all a,b,c
                # 2. Adding 1 because array is 0-based
                # 3. This count represents all possible substrings ending at current position 
                count = count + (1 + min(last_seen))

        return count