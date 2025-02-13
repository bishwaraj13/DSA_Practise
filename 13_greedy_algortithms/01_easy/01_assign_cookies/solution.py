# https://leetcode.com/problems/assign-cookies/
from typing import *

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l = 0 # pointer to cookies size (s)
        r = 0 # pointer to greed (g)
        g.sort()
        s.sort()

        while l < len(s) and r < len(g):
            if g[r] <= s[l]:
                l += 1
                r += 1
            else:
                # cookies is smaller, so we go to next size
                l += 1

        return r
        