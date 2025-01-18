// https://leetcode.com/problems/reverse-integer/
// In leetcode, it is required to return 0 when the reversed number is out of the range of 32-bit signed integer.
// to check if the reversed number is out of the range, we can use the following code:
// if (reversed_num > Integer.MAX_VALUE || reversed_num < Integer.MIN_VALUE) return 0;
// Also, we need to take care of the negative numbers, because the condition num > 0 will not work for negative numbers.
class Solution {
    public int reverse(int x) {
        int reversed_num = 0;
        int num = x;

        while (num > 0) {
            reversed_num = reversed_num * 10 + num % 10;
            num = num / 10;
        }

        return reversed_num;
    }
}