"""
863. All Nodes Distance K in Binary Tree
Solved
Medium
Topics
Companies
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Time Complexity: O(N) for dfs + O(N) for bfs = O(N)
        # Space Complexirt: O(E) = O(N-1) = O(N) , Edges = Number of nodes - 1 (property if a tree)
        # edge case
        if k == 0:
            return [target.val]
        adj_list = defaultdict(list)

        # we use dfs(could use bfs as well) to traverse all the nodes and create a adj_list
        def dfs(prev,node):
            if node == None:
                return
            if prev is not None:
                adj_list[prev.val].append(node.val)
                adj_list[node.val].append(prev.val)
            dfs(node, node.left)
            dfs(node,node.right)

        # to keep track if we reach the required distance
        steps=1
        queue = deque([target.val])

        # run the dfs to populate ajd adj list
        dfs(None,root)
        # to keep track of already visited nodes
        visited = set()
        visited.add(target.val)
        res = []
        # bfs
        while queue and steps <= k:
            for _ in range(len(queue)):
                node_val = queue.popleft()
                for nei_val in adj_list[node_val]:
                    if nei_val not in visited:
                        queue.append(nei_val)
                        visited.add(nei_val)
                        if steps == k:
                            res.append(nei_val)
            steps+=1
      

        return res
