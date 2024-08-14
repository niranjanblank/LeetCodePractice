"""

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right\

# transverse the entire tree
# recursive solution
class Solution1:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # to store the sorted data
        inOrder = []

        def dfs(curr):
            if not curr:
                return

            # perforrm dfs on left tree
            dfs(curr.left)
            # add current value in the inOrder
            inOrder.append(curr.val)
            # perform dfs on right tree
            dfs(curr.right)

        dfs(root)
        return inOrder[k - 1]


# iterative solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize an empty stack to aid in iterative in-order traversal
        stack = []
        # Initialize a counter to keep track of how many nodes have been visited
        n = 0

        # Start the traversal with the root node
        curr = root

        # Perform in-order traversal: left -> root -> right
        while stack or curr:
            # Traverse to the leftmost node, as it will have the smallest value in a BST
            while curr:
                stack.append(curr)  # Add the current node to the stack
                curr = curr.left  # Move to the left child

            # Pop the node from the stack, which is the next smallest element
            curr = stack.pop()
            n += 1  # Increment the count of nodes visited

            # If we've visited k nodes, the current node is the kth smallest
            if n == k:
                return curr.val  # Return the value of the kth smallest node

            # Move to the right subtree, as it contains the next larger elements
            curr = curr.right
