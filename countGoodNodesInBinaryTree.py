"""
1448. Count Good Nodes in Binary Tree
Medium
Topics
Companies
Hint
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.



Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def dfs(node, maxSoFar):
#     if not node:
#         return 0
#     if node.val >= maxSoFar:
#         good = 1
#     else:
#         good = 0
#     maxSoFar = max(node.val, maxSoFar)
#     good += dfs(node.left, maxSoFar)
#     good += dfs(node.right, maxSoFar)
#     return good
#
# def goodNodes(root):
#     return dfs(root, root.val)


# Helper function to build the tree from a list
def buildTree(values):
    nodes = [None if val is None else TreeNode(val) for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

tree1 = buildTree([3,1,4,3,None,1,5])


def goodNodes(root):
    return dfs(root, root.val)

def dfs(node, maxSoFar):

    if not node:
        return 0

    if node.val >= maxSoFar:
        good = 1
    else:
        good = 0


    # transversion left
    good += dfs(node.left, maxSoFar)
    # transversion right
    good += dfs(node.right, maxSoFar)

    return good
print(goodNodes(tree1))



