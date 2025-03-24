# https://leetcode.com/problems/shortest-palindrome/
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix = 0
        reversed_prefix = 0
        base = 29
        last_index = 0
        mod = 10**9 + 7
        power = 1

        # The intution can be better understood in form of numbers
        # Say we have string s = "12145". The number has palindrome prefix: "121".
        # We set out to find palindrome prefix
        for i, c in enumerate(s):
            # in each iteration, we try to find if string till i-th index is palindrome
            # in iteration 0, we are finding if "1" is palindrome
            # in iteration 1, we are finding if "12" is palindrome 
            # in iteration 3, we find out that "121" is palindrome
            ch_int = (ord(c) - ord('a') + 1)

            # to identify palindrome, we once read string from left-to-right, we call it prefix
            # we again read it from right-to-left, we call it reversed_prefix

            # say base=10, s = "123", prefix = 0
            # i=0, ch=1, prefix = (prefix*10)+ch = (0*10)+1 = 1
            # i=1, ch=2, prefix = (prefix*10)+ch = (1*10)+2 = 12
            # i=2, ch=3, prefix = (prefix*10)+ch = (12*10)+3 = 123
            prefix = (prefix * base) % mod
            prefix = (prefix + ch_int) % mod

            # say base=10, s="123", reversed_prefix=0
            # i=0, ch=1, reversed_prefix = (ch*10^i)+reversed_prefix = (1*10^0)+0 = 1
            # i=1, ch=2, reversed_prefix = (ch*10^i)+reversed_prefix = (2*10^1)+1 = 21
            # i=2, ch=3, reversed_prefix = (ch*10^i)+reversed_prefix = (3*10^2)+21 = 321
            # reversed_prefix = (ch_int * (base**i) + reversed_prefix) % mod
            reversed_prefix = (ch_int * power + reversed_prefix) % mod
            power = (power * base) % mod

            if prefix == reversed_prefix:
                last_index = i

        suffix = s[last_index+1:]
        return suffix[::-1] + s