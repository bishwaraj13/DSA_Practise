# https://www.naukri.com/code360/problems/boundary-traversal_790725
# technique:
# step 1: traverse left boundary excluding leaf
# step 2: leaf nodes (do inorder traversal, and insert whichever are leaf nodes)
# step 3: right boundary in the reverse
'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# Functions to traverse on each part.
def traverseBoundary(root):
    if not root:
        return []

    result = []
    # add root value
    result.append(root.data)

    # traverse left boundary
    addLeftBoundary(root, result)
    # add leaves
    inorderAddLeaves(root, result)
    # add right boundary
    addRightBoundary(root, result)

    return result

## helper functions ##
def addLeftBoundary(root, result):
    root = root.left

    while root:
        # check if not leaf node
        if root.left or root.right:
            result.append(root.data)
        
        if root.left:
            root = root.left
        else:
            root = root.right

def addRightBoundary(root, result):
    root = root.right
    stack = []

    while root:
        # check if not leaf node
        if root.left or root.right:
            stack.append(root.data)

        if root.right:
            root = root.right
        else:
            root = root.left

    while stack:
        result.append(stack.pop())

def inorderAddLeaves(root, result):
    if not root.left and not root.right:
        result.append(root.data)
        return

    if root.left:
        inorderAddLeaves(root.left, result)
    # unlike inorder, we dont have to add root
    if root.right:
        inorderAddLeaves(root.right, result)
