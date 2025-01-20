class Solution:
 
    def mergeSort(self,arr, l, r):
        # handle invalid case
        if l > r:
            return []
            
        if l == r:
            return [arr[l]]
            
        m = (l + r) // 2
        
        return self.mergeSortedArrays(
            self.mergeSort(arr, l, m), 
            self.mergeSort(arr, m+1, r)
            )
        
    def mergeSortedArrays(self, arr1, arr2):
        index1, index2 = 0, 0
        result_arr = []
        
        while index1 < len(arr1) and index2 < len(arr2):
            if arr1[index1] < arr2[index2]:
                result_arr.append(arr1[index1])
                index1 += 1
            else:
                result_arr.append(arr2[index2])
                index2 += 1
                
       
        result_arr.extend(arr1[index1:])
        result_arr.extend(arr2[index2:])
        
        return result_arr
    

solution = Solution()
your_array = [4, 1, 3, 9, 7]
result = solution.mergeSort(your_array, 0, len(your_array)-1)
print(result)