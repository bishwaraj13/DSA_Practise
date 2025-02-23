# https://www.geeksforgeeks.org/problems/largest-bst/1
class NodeValue:
    def __init__(self, minNode, maxNode, bstSize):
        self.minNode = minNode
        self.maxNode = maxNode
        self.bstSize = bstSize

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
class Solution:
    def largestBst(self, root):
        # Your code here
        def dfs(node):
            if not node:
                return NodeValue(float("inf"), float("-inf"), 0)
                
            # get values from left and right subtree of node
            left = dfs(node.left)
            right = dfs(node.right)
            
            # if curr node is greater than max of left, and min of right,
            # its a valid BST
            if left.maxNode < node.data and node.data < right.minNode:
                return NodeValue(
                        min(node.data, left.minNode),
                        max(node.data, right.maxNode),
                        1 + left.bstSize + right.bstSize
                    )
                    
            # otherwise its not valid BST
            # so we return maxNode as float("-inf") and vice versa
            return NodeValue(
                    float("-inf"),
                    float("inf"),
                    max(left.bstSize, right.bstSize)
                )
                    
        result = dfs(root)
        return result.bstSize
    

root = TreeNode(
    20,    
    TreeNode(
        15, 
        TreeNode(14, None, TreeNode(17)),
        TreeNode(18, TreeNode(10), TreeNode(19))
        ),
    TreeNode(
        40,
        TreeNode(30),
        TreeNode(60, TreeNode(50))
    )    
    )

bst_size = Solution().largestBst(root)

print(bst_size)