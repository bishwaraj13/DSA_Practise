// https://www.geeksforgeeks.org/problems/frequency-of-array-elements-
class Solution {
    // Function to count the frequency of all elements from 1 to N in the array.
    public List<Integer> frequencyCount(int[] arr) {
        ArrayList<Integer> result = new ArrayList<>();
        
        for (int i = 0; i < arr.length; i++) {
            result.add(0);
        }
        
        for (int element: arr) {
            result.set(element-1, result.get(element-1) + 1);
        }
        
        return result;
    }
}