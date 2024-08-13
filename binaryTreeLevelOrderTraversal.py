"""

Test Result
102. Binary Tree Level Order Traversal
Solved
Medium
Topics
Companies
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #    variable to store the result
        result = []

        # queue for bfs
        queue = collections.deque()
        # adding the root node to the queue initially
        queue.append(root)
        # running the loop until the queue is empty, meaning we have traversed through all the nodes
        while queue:
            # get length of the queue to get the values of nodes from the current level
            queue_length = len(queue)

            # array to store values in current level
            level = []

            # iterating using the queue_length and adding all the nodes in current level
            for i in range(queue_length):
                # poping the node from queue
                node = queue.popleft()
                # if the node is not null, we add it to the level
                if node:
                    level.append(node.val)
                    # adding the child of the node in the queue
                    # if the left and right nodes are none,
                    # they would be initially added to the queue
                    # but when popped they will be none so it wont be added to the level
                    queue.append(node.left)
                    queue.append(node.right)
            # if level is not empty we, add it to the result
            if level:
                result.append(level)

        return result