"""
429. N-ary Tree Level Order Traversal
Solved
Medium
Topics
Companies
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Time Complexity(O(n))
        # Space Complexity(O(n))
        # if the node is None, return empty result
        if not root:
            return []

        # queue for bfs
        queue = deque()
        queue.append(root)
        # to store the result
        res = []

        while queue:
            # we get the queue length, to visit all the elements at the curr level
            queue_len = len(queue)

            elem = []
            # visiting all the nodes in current level
            for _ in range(queue_len):
                item = queue.popleft()
                elem.append(item.val)
                # add all the childrens to the queue
                for child in item.children:
                    queue.append(child)
            res.append(elem)

        return res
