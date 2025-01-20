class Solution:
    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2
            
            # Recursively sort left and right halves
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            
            # Merge the sorted halves
            self.merge(arr, l, mid, r)
            
    def merge(self, arr, l, mid, r):
        # Create temporary arrays only for merging
        left = arr[l:mid + 1]
        right = arr[mid + 1:r + 1]
        
        i = j = 0
        k = l
        
        # Merge back into original array
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        # Copy remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

solution = Solution()
your_array = [4, 1, 3, 9, 7]
solution.mergeSort(your_array, 0, len(your_array)-1)
print(your_array)
