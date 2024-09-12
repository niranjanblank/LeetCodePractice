"""
3651 · Number of Connected Components in an Undirected Graph
Algorithms
Medium
Accepted Rate
54%

Description
Solution23
Notes
Discuss5
Leaderboard
Record
Description
In this problem, there is an undirected graph with n nodes. There is also an edges array. Where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

You need to return the number of connected components in that graph.

Example
Example 1

Input:

3
[[0,1], [0,2]]
Output:

1
Example 2

Input:

6
[[0,1], [1,2], [2, 3], [4, 5]]
Output:

2
"""

from typing import List

class Solution1:
    # using dfs
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_map = {i: [] for i in range(n)}

        for edge in edges:
            adj_map[edge[0]].append(edge[1])
            adj_map[edge[1]].append(edge[0])

        visited = set()

        def dfs(i):
            if i in visited:
                return False

            visited.add(i)

            # goint through  each neighbour
            for item in adj_map[i]:
                if item in visited:
                    continue
                dfs(item)

        total_comp = 0
        for item in range(n):
            if item not in visited:
                dfs(item)
                total_comp += 1

        return total_comp

# if we want to keep track of components as well
class Solution2:
    # using dfs and tracking structure of connected components
    def countComponents(self, n: int, edges: List[List[int]]) -> (int, List[List[int]]):
        adj_map = {i: [] for i in range(n)}

        # Build adjacency list
        for edge in edges:
            adj_map[edge[0]].append(edge[1])
            adj_map[edge[1]].append(edge[0])

        visited = set()
        components = []  # To store the structure of each component

        def dfs(i, component):
            if i in visited:
                return

            visited.add(i)
            component.append(i)

            # Go through each neighbor
            for neighbor in adj_map[i]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        total_comp = 0
        for node in range(n):
            if node not in visited:
                component = []  # New component
                dfs(node, component)
                components.append(component)
                total_comp += 1

        return total_comp, components  # Return both count and the components

class Solution3:
    # using union find
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass


# Example usage
sol = Solution2()
n = 6
edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
count, components = sol.countComponents(n, edges)
print("Number of connected components:", count)
print("Connected components structure:", components)