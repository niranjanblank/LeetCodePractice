# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize the node with a value, and optional left and right children.
        self.val = val
        self.left = left
        self.right = right

# Function to calculate the maximum depth of a binary tree.
def maxDepth(root):
    # Base case: if the current node is None, the depth is 0.
    if root is None:
        return 0
    else:
        # Recursively calculate the depth of the left subtree.
        left_depth = maxDepth(root.left)
        # Recursively calculate the depth of the right subtree.
        right_depth = maxDepth(root.right)
        # The maximum depth of the current tree is the max of left and right depths plus one for the current node.
        return max(left_depth, right_depth) + 1

# Example usage:

# Constructing the binary tree from the given example:
#       3
#      / \
#     9  20
#       /  \
#      15   7

# Create the root node with value 3.
root = TreeNode(3)
# Create the left child of the root node with value 9.
root.left = TreeNode(9)
# Create the right child of the root node with value 20.
root.right = TreeNode(20)
# Create the left child of the node with value 20, with value 15.
root.right.left = TreeNode(15)
# Create the right child of the node with value 20, with value 7.
root.right.right = TreeNode(7)

# Call the maxDepth function with the root of the tree and print the result.
print(maxDepth(root))  # Output: 3

# This prints the maximum depth of the binary tree, which is 3 in this example.
