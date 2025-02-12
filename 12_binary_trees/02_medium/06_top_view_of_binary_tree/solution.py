# https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
# built on ideas of vertical order traversal
# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
from collections import deque

class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        if not root:
            return []
        result = []
        queue = deque()
        queue.append((root, 0))
        vertical_dict = {}
        
        while queue:
            queue_size = len(queue)
            
            for i in range(queue_size):
                curr, line = queue.popleft()
                
                if line not in vertical_dict:
                    vertical_dict[line] = curr.data
                
                if curr.left:
                    queue.append((curr.left, line-1))
                if curr.right:
                    queue.append((curr.right, line+1))
                    
        for key in sorted(vertical_dict.keys()):
            result.append(vertical_dict[key])
            
        return result