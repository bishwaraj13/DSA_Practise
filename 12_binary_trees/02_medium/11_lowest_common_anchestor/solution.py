# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, values):
            if node.val in values:
                return node

            # leaf node?
            if not node.left and not node.right:
                return None

            node1 = None
            if node.left:
                node1 = dfs(node.left, values)

            node2 = None
            if node.right:
                node2 = dfs(node.right, values)

            if node1 and node2:
                return node
            elif node1:
                return node1
            elif node2:
                return node2
 
            return None

        lca = dfs(root, [p.val, q.val])

        return lca
        