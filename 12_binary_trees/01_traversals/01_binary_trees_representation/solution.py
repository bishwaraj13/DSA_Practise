class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create the root node
root = Node(1)

# Create and attach left and right children to root
root.left = Node(2)
root.right = Node(3)

# Add children to the left node
root.left.left = Node(4)
root.left.right = Node(5)

# Add children to the right node
root.right.left = Node(6)
root.right.right = Node(7)