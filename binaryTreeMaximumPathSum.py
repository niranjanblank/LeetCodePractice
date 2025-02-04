"""
124. Binary Tree Maximum Path Sum
Solved
Hard
Topics
Companies
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #Time Complexity : O(n)
        #Space Complexity: O(n)
        res = float('-inf')
        def dfs(node):
            nonlocal res
            if node is None:
                return 0

            # maximum values we can get from left and right subarray
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            # to discard negative values
            left_val = max(left_val,0)
            right_val = max(right_val,0)

            # we store just the maximum value of node + max val form one of its childrens
            res = max(res, node.val+left_val+right_val)
            # for each node, we just return the sum of the node and one of its childs value
            # this is because a path can only extend in one direction (either left or right)
            return node.val + max(left_val, right_val)

        dfs(root)

        return res
