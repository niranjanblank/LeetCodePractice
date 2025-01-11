"""
116. Populating Next Right Pointers in Each Node
Solved
Medium
Topics
Companies
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Time complexity: O(n)
        # Space complexity: O(n)
        if not root:
            return root

        queue = deque()
        queue.append(root)
        while queue:
            queue_length = len(queue)
            for i in range(queue_length):
                # items would be population in the queue from left to right
                item = queue.popleft()
                # if there are item in the queue, then the next of current item can be the first element of 
                # queue
                if i+1<queue_length:
                    item.next = queue[0]
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
        return root

class Solution2:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Time complexity: O(n)
        # Space complexity: O(1)
        if not root:
            return root

        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                # items would be population in the queue from left to right
                head.left.next = head.right
                # connect the rigfht child to the next subtree's left child
                if head.next:
                    head.right.next = head.next.left
                # move to the next node in the current level
                head = head.next
            # move to next level
            leftmost = leftmost.left
        return root
