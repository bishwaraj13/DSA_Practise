// bubble sort
class Solution {
    // Function to sort the array using bubble sort algorithm.
    public static void bubbleSort(int arr[]) {
        int total_indexes = arr.length - 1;
        
        while (total_indexes>=0) {
            // After every for loop, 
            // the last_index gets updated with largest number
            for (int i=1; i<=total_indexes; i++) {
                if (arr[i] < arr[i-1]) {
                    // swap arr[i] and arr[i-1]
                    int temp = arr[i];
                    arr[i] = arr[i-1];
                    arr[i-1] = temp;
                }
            }
            
            total_indexes--;
        }
    }
}