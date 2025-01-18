# https://leetcode.com/problems/reverse-integer/
# In leetcode, it is required to return 0 when the reversed number is out of the range of 32-bit signed integer.
# to check if the reversed number is out of the range, we can use the following code:
# if (reversed_num > Integer_MAX_VALUE or reversed_num < Integer_MIN_VALUE) return 0;
# you can actually compute integer_MAX_VALUE and integer_MIN_VALUE by using the following code: 2**31 - 1 and -2**31
# Also, we need to take care of the negative numbers, because the condition num > 0 will not work for negative numbers.
class Solution:
    def reverse(self, x: int) -> int:
        num = x
        reversed_num = 0

        while num > 0:
            reversed_num = reversed_num * 10 + num % 10
            num = num // 10

        return reversed_num