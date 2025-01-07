"""
1466. Reorder Routes to Make All Paths Lead to the City Zero
Solved
Medium
Topics
Companies
Hint
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

 

Example 1:


Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 2:


Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
 

Constraints:

2 <= n <= 5 * 104
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
"""
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Time Complexity: O(V+E)
        # Space Companies: O(V+E)
        # creating the adjacency list
        adj_list = defaultdict(list)
        # creating edges set for quick look up O(1) time complexity
        edges = set()
        for a,b in connections:
            # we create undirected graph
            adj_list[a].append(b)
            adj_list[b].append(a)
            edges.add((a,b))

        # to keep track of changes we need to make
        self.changes = 0
        
        visited = set()
        def dfs(prev,curr):
            if curr in visited:
                # if we have visited the node already we dont need to visit it again
                return
            visited.add(curr)
            if (prev, curr) in edges:
                # if the edge is in forward direction, we need to reverse it to point to 0
                # so increases the changes required
                self.changes+=1
            for neigh in adj_list[curr]:
                # going through the child components
                dfs(curr, neigh)

        # starting dfs with -1 as prev node , and 0 as curr node
        dfs(-1,0)

        return self.changes

