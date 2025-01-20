// https://www.geeksforgeeks.org/problems/reverse-an-array/0
class Solution {
    public void reverseArray(int arr[]) {
        reverseArrayRecursive(arr, 0, arr.length-1);
    }
    
    public void reverseArrayRecursive(int arr[], int left, int right) {
        if (left >= right) {
            return;
        }
        
        // swap value at index left and index right
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        
        reverseArrayRecursive(arr, left+1, right-1);
    }
}