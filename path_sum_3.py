"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).



Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):

    def dfs(node, currentSum, pathCounts):
        if node is None:
            return 0

        currentSum += node.val
        sumCount = pathCounts.get(currentSum - targetSum, 0)

        pathCounts[currentSum] = pathCounts.get(currentSum, 0) + 1

        leftCount = dfs(node.left, currentSum, pathCounts)
        rightCount = dfs(node.right, currentSum, pathCounts)

        pathCounts[currentSum] = pathCounts[currentSum] - 1

        return sumCount + leftCount + rightCount

    if not root:
        return 0

    return dfs(root, 0 , {0:1})