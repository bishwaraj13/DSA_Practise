# Sorting Algorithms Cheatsheet

| Algorithm      | Description                                                                                                                                                                                                                  | Time Complexity                   |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| Selection Sort | • Repeatedly finds minimum element from unsorted portion<br>• Places it at beginning of array<br>• Builds sorted portion left to right<br>• In-place comparison sort [[1]]<br>• Simple but inefficient for large lists [[6]] | O(n²) [[2]]                       |
| Bubble Sort    | • Repeatedly steps through list<br>• Compares adjacent elements<br>• Swaps if in wrong order<br>• Larger elements "bubble up" to end<br>• Multiple passes until sorted                                                       | O(n²)                             |
| Insertion Sort | • Maintains sorted portion at start<br>• Takes one unsorted element at a time<br>• Inserts it into correct position in sorted portion<br>• Shifts elements as needed                                                         | O(n²)                             |
| Merge Sort     | • Divide-and-conquer algorithm<br>• Recursively splits array in half<br>• Merges sorted subarrays<br>• Uses two-pointer technique<br>• Stable sort                                                                           | O(n log n)                        |
| Quick Sort     | • Divide-and-conquer algorithm<br>• Selects pivot element<br>• Partitions array around pivot<br>• Recursively sorts subarrays<br>• In-place sorting                                                                          | O(n log n) average<br>O(n²) worst |

### Key Points:

- Selection, Bubble, and Insertion sorts are simpler but less efficient (O(n²))
- Merge and Quick sorts are more efficient (O(n log n)) but more complex
- Selection sort is notable for simplicity but performs worse than insertion sort [[6]]
