"""
110. Balanced Binary Tree
Solved
Easy
Topics
Companies
Given a binary tree, determine if it is
height-balanced
.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution one
class Solution1:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.res = True

        def dfs(curr):
            # if self.res has already bet found to be False, we can just return 0, as going through
            # all the subtrees wont change the result
            if not self.res:
                return 0

            if curr is None:
                return 0

            left_depth = dfs(curr.left)
            right_depth = dfs(curr.right)

            if abs(left_depth - right_depth) > 1:
                self.res = False

            return max(left_depth, right_depth) + 1

        dfs(root)

        return self.res

# solution two

class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def dfs(curr):
            if curr is None:
                return [True,0]

            left_depth = dfs(curr.left)
            right_depth = dfs(curr.right)

            balanced = left_depth[0] and right_depth[0] and abs(left_depth[1] - right_depth[1]) <= 1

            return [balanced,max(left_depth[1], right_depth[1]) + 1]



        return dfs(root)[0]

