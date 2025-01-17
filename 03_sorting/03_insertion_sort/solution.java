// insertion sort
class Solution {
    public void insertionSort(int arr[]) {
        int sorted_till = 0;
        
        while (sorted_till < arr.length - 1) {
            // take next-index whose value needs to be inserted
            int next = sorted_till + 1;
            
            while ((next > 0) && (arr[next] < arr[next-1])) {
                // swap values at "next" and "next-1"
                int temp = arr[next];
                arr[next] = arr[next-1];
                arr[next-1] = temp;
                
                next -= 1;
            }
            
            // at end of while loop the sorted subset array length increases by 1
            sorted_till += 1;
        }
    }
}