# https://leetcode.com/problems/longest-common-prefix/
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        counter = 0
        substring = ""

        if not strs:
            return substring

        while True:
            first_str = strs[0]

            if counter < len(first_str):
                ch = first_str[counter]
            else:
                return substring

            for i in range(1, len(strs)):
                current_str = strs[i]

                if counter > len(current_str)-1 or current_str[counter] != ch:
                    return substring

            counter += 1
            substring = substring + ch

        return substring    