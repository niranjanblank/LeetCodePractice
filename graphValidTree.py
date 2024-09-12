"""
Description
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.



You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example
Example 1:

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
Example 2:

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # checking if the number of vertices is 0
        if not n:
            return True

        # creating an empty adjacency map to store the adjacent vertices of all the nodes
        adj_map = {i: [] for i in range(n)}

        # filling the adj_map
        for edge in edges:
            adj_map[edge[0]].append(edge[1])
            adj_map[edge[1]].append(edge[0])

        # creating a hashset to keep track of visited nodes
        visited = set()

        def dfs(i, prev):
            # prev is supplied as the edges are undirected
            if i in visited:
                # cycle detected
                return False

            # if no cycle detected, add it to the visited hashset
            visited.add(i)

            # iterating through each adjacent vertices of the current node
            for item in adj_map[i]:
                # if this item is the prev node of current node, we ignore it
                if item == prev:
                    continue
                if not dfs(item, i):
                    return False

            # if all the nodes can be iterated, then current node is valid
            return True

        return dfs(0, -1) and len(visited) == n