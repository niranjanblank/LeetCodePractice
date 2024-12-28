"""
797. All Paths From Source to Target
Solved
Medium
Topics
Companies
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
"""


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # For a DAG, there could be at most 2^(V-1) - 1 possible paths to go fromm starting vertex to target vertex
        # We need O(V) to build each such paths. So overall time complexity will be O(2^V.V)
        #Time Complexity: O(2^V.V)
        #Space Complexity: O(V+E)
        adj_list = defaultdict(list)
        end = len(graph) - 1
        for i,nodes in enumerate(graph):
            adj_list[i].extend(nodes)
        
        paths = []
        curr_path = []

        def dfs(node):
            curr_path.append(node)
            if node == end:
                paths.append(curr_path.copy())

            for neigh in adj_list[node]:
                dfs(neigh)
                curr_path.pop()
        dfs(0)

      
        return paths
