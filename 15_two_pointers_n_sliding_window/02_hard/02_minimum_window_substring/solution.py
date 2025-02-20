# https://leetcode.com/problems/minimum-window-substring/
# solution explanation: https://www.youtube.com/watch?v=WJaij9ffOIY
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Handle empty string cases
        if not s or not t:
            return ""

        # Initialize hash map with 256 zeros (for ASCII characters)
        hash_map = [0] * 256

        l = 0
        r = 0
        start_index = -1
        min_len = float("inf")
        count = 0

        # get length of string
        n, m = len(s), len(t)

        # fill hashmap
        for char in t:
            hash_map[ord(char)] += 1

        # sliding window approach
        while r < n:
            # process right pointer
            if hash_map[ord(s[r])] > 0:
                count += 1
            
            hash_map[ord(s[r])] -= 1

            # check if we have all characters from t
            while count == m:
                # update min window if current window is smaller
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start_index = l


                # process left pointer
                hash_map[ord(s[l])] += 1
                if hash_map[ord(s[l])] > 0:
                    count -= 1

                l += 1
            r += 1

        return "" if start_index == -1 else s[start_index:start_index+min_len]