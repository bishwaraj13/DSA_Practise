// https://www.geeksforgeeks.org/problems/count-digits5716/1
class Solution {
    static int evenlyDivides(int n) {
        int quotient = n;
        int count = 0;
        
        while (quotient > 0) {
            int digit = quotient % 10;
            
            if (digit != 0 && n % digit == 0) {
                count += 1;
            }
            
            quotient = quotient / 10;
        }
        
        return count;
    }
}