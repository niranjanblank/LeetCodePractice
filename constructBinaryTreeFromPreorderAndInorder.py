"""
Test Result
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium
Topics
Companies
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if any of preorder or inorder is empty, the tree cannot be built
        if not preorder or not inorder:
            return None
        # first element of preorder is always root of tree
        root = TreeNode(preorder[0])
        # root of tree is always the mid of inorder, so we get mid index here
        # all the items on the left of inorder belong to left subtree
        # all the items on the right of inorder belong to right subtree
        mid = inorder.index(preorder[0])

        # the length of items from 0 to mid of inorder gives total items in left subtree
        # so we can get 1:mid+1 elements from preorder, which belong to left subtree
        # we start from 1 as at 0 index, we have the root of that subtree
        # similarly, for inder all the items till mid elements are in left subtree
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # for right subtree, all the items that doesnt belong to left belong to right
        # so for preorder its mid+1: (which means from mid+1 to end)
        # for inorder its mid+1: end as well
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root