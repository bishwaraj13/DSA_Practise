# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = {}
        t_to_s = {}

        for s_ch, t_ch in zip(s, t):
            if s_ch not in s_to_t and t_ch not in t_to_s:
                s_to_t[s_ch] = t_ch
                t_to_s[t_ch] = s_ch
            else:
                if (s_ch not in s_to_t or 
                t_ch not in t_to_s or 
                s_to_t[s_ch] != t_ch or 
                t_to_s[t_ch] != s_ch):
                    return False

        return True

        