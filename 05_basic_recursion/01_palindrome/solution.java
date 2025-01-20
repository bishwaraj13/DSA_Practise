// https://leetcode.com/problems/valid-palindrome/
class Solution {
    public boolean isPalindrome(String s) {
        String cleanStr = s.toLowerCase().replaceAll("[^a-z0-9]", "");
        return isPalindromeRecursive(cleanStr, 0, cleanStr.length()-1);
    }

    public boolean isPalindromeRecursive(String s, int left, int right) {
        if (left >= right) {
            return true;
        }
        
        if (s.charAt(left) != s.charAt(right)) {
            return false;
        }

        return isPalindromeRecursive(s, left+1, right-1);
    }
}