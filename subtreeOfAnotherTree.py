"""
572. Subtree of Another Tree
Easy
Topics
Companies
Hint
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.



Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false


Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# method one, checking for is Same
class Solution:
    def isSame(self, p, q):
        if p is None and q is None:
            return True
        elif (p is None) or (q is None) or p.val != q.val:
            return False
        else:
            left_match = self.isSame(p.left, q.left)
            right_match = self.isSame(p.right, q.right)
        return left_match and right_match

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False

        def dfs(curr, subRoot):
            if self.res:
                return

            if curr is None:
                return

            if self.isSame(curr, subRoot):
                self.res = True
                return

            dfs(curr.left, subRoot)
            dfs(curr.right, subRoot)

        dfs(root, subRoot)
        return self.res


# solution two
class Solution2:
    def isSame(self, p, q):
        if p is None and q is None:
            return True
        elif (p is None) or (q is None) or p.val != q.val:
            return False
        else:
            left_match = self.isSame(p.left, q.left)
            right_match = self.isSame(p.right, q.right)
        return left_match and right_match

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None: return True
        if root is None: return False

        if self.isSame(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))