"""
543. Diameter of Binary Tree
Easy
Topics
Companies
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum diameter to 0
        # This variable will store the longest path found during DFS
        self.res = 0

        def dfs(curr):
            """
            Helper function to perform DFS on the tree.

            Args:
                curr (TreeNode): The current node being visited.

            Returns:
                int: The height of the subtree rooted at the current node.
            """
            # Base case: if the current node is None, return 0
            # This represents the height of an empty subtree
            if not curr:
                return 0

            # Recursively calculate the height of the left subtree
            left_height = dfs(curr.left)
            # Recursively calculate the height of the right subtree
            right_height = dfs(curr.right)

            # Update the maximum diameter found so far
            # The diameter at the current node is the sum of the heights of the left and right subtrees
            # Update self.res if the current diameter is larger
            self.res = max(self.res, left_height + right_height)

            # Return the height of the subtree rooted at the current node
            # This height is the maximum of the heights of the left and right subtrees plus 1
            # The +1 accounts for the current node itself
            return max(left_height, right_height) + 1

        # Start DFS from the root node to compute the diameter
        dfs(root)

        # Return the maximum diameter found
        return self.res