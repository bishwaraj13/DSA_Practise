# https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def Paths(self, root):
        if not root:
            return []
        all_paths = []

        def get_path(node, path):
            path.append(node.data)
            
            # check if we reached leaf node
            if not node.left and not node.right:
                all_paths.append(path.copy())
            
            if node.left:
                get_path(node.left, path)
                
            if node.right:
                get_path(node.right, path)
            
            # backtrack by popping this node
            path.pop()
        
        get_path(root, [])
        return all_paths