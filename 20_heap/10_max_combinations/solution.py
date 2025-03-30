# https://www.geeksforgeeks.org/problems/maximum-sum-combination/0
class Solution:
    def maxCombinations(self, N, K, A, B):
        # Sort both arrays in descending order
        A.sort(reverse=True)
        B.sort(reverse=True)
        
        # Use a max heap to keep track of the largest combinations
        import heapq
        max_heap = []
        
        # Set to keep track of indices we've already considered
        visited = set()
        
        # Start with the combination of the largest elements
        heapq.heappush(max_heap, (-(A[0] + B[0]), 0, 0))
        visited.add((0, 0))
        
        result = []
        
        # Extract K maximum combinations
        while max_heap and len(result) < K:
            # Negative sum to simulate max heap, along with indices i, j
            neg_sum, i, j = heapq.heappop(max_heap)
            current_sum = -neg_sum
            
            # Add to result
            result.append(current_sum)
            
            # Try the next combinations: (i+1,j) and (i,j+1)
            if i + 1 < N and (i + 1, j) not in visited:
                heapq.heappush(max_heap, (-(A[i + 1] + B[j]), i + 1, j))
                visited.add((i + 1, j))
                
            if j + 1 < N and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-(A[i] + B[j + 1]), i, j + 1))
                visited.add((i, j + 1))
                
        return result