// https://leetcode.com/problems/palindrome-number/submissions/1512166127/

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int reversed_num = 0;
        int temp = x;

        while (temp > 0) {
            reversed_num = reversed_num * 10 + temp % 10;
            temp = temp / 10;
        }

        if (reversed_num == x) {
            return true;
        }

        return false;
    }
}