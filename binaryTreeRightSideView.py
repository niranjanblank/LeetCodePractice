"""
199. Binary Tree Right Side View
Solved
Medium
Topics
Companies
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # list to store the value of the right view nodes
        result = []

        # creating queue for bfs
        queue = collections.deque()

        # adding the root node to the queue
        queue.append(root)

        while queue:
            # this is store the node which can be viewed from right
            right_view_node = None
            # length of queue to transverse through the queue
            queue_length = len(queue)

            for i in range(queue_length):
                node = queue.popleft()
                # if the right most elements in the current queue are node, we just ignore them
                if node:
                    right_view_node = node
                    # adding the child of this node to queue
                    queue.append(node.left)
                    queue.append(node.right)

            if right_view_node:
                result.append(right_view_node.val)

        return result


class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        # list to store the value of the right view nodes
        result = []

        # creating queue for bfs
        queue = collections.deque()

        # adding the root node to the queue
        queue.append(root)

        while queue:

            # length of queue to transverse through the queue
            queue_length = len(queue)

            for i in range(queue_length):
                node = queue.popleft()

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            result.append(node.val)

        return result