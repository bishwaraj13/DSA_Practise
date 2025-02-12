# https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
# this solution is built on top of vertical order traversal
from collections import deque

class Solution:
    def bottomView(self, root):
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
                    vertical_dict[line] = [curr.data]
                else:
                    temp_list = vertical_dict[line]
                    temp_list.append(curr.data)
                
                if curr.left:
                    queue.append((curr.left, line-1))
                if curr.right:
                    queue.append((curr.right, line+1))
                    
        for key in sorted(vertical_dict.keys()):
            result.append(vertical_dict[key][-1])
            
        return result