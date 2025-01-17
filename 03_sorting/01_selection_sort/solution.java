// selection sort
class Solution {
    void selectionSort(int[] arr) {
        for(int i=0; i<arr.length; i++) {
            // find minimum from i to length-of-array
            int min_index = i;
            for (int j=i+1; j<arr.length; j++) {
                if (arr[j] < arr[min_index]) {
                    min_index = j;
                }
            }
            
            // we found min_index has the least value,
            // so we swap arr[i] with arr[min_index]
            int temp_val = arr[i];
            arr[i] = arr[min_index];
            arr[min_index] = temp_val;
        }
    }
}