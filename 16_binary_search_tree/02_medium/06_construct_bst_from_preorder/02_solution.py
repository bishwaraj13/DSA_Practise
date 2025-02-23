from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        inorder = sorted(preorder)
        return self.buildTree(preorder, inorder)
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        rootVal = preorder[0]

        # get index of the root in inorder
        root_index_inorder = inorder.index(rootVal)

        # get inorder of left subtree
        left_subtree_inorder = inorder[:root_index_inorder]

        # get inorder of right subtree
        right_subtree_inorder = inorder[root_index_inorder+1:]

        # get preorder of left subtree
        left_subtree_preorder = preorder[1:1+len(left_subtree_inorder)]

        # get preorder of right subtree
        right_subtree_preorder = preorder[1+len(left_subtree_inorder):]

        # create root node
        root = TreeNode(rootVal)

        root.left = self.buildTree(left_subtree_preorder, left_subtree_inorder)
        root.right = self.buildTree(right_subtree_preorder, right_subtree_inorder)

        return root
