"""
1971. Find if Path Exists in Graph
Solved
Easy
Topics
Companies
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
 

Constraints:

1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.
"""
class SolutionRecursiveDFS:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list  = defaultdict(list)

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if node == destination:
                return True
            visited.add(node)

            for neigh in adj_list[node]:
                if dfs(neigh):
                    return True

            return False
    
        return dfs(source)


class SolutionIterativeDFS:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Create adjacency list
        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        visited = set()
        stack = []
        stack.append(source)

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                stack.extend(adj_list[node])

        return False
            

class UnionFind:
    def __init__(self,n):
        self.rank = [1]*n
        self.root = [i for i in range(n)]

    def find(self,x):
        if x!=self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_y] > self.rank[root_x]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] +=1
    
    def connected(self,x,y):
        return self.find(x) == self.find(y)

class SolutionUnionFind:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        uf = UnionFind(n)

        for edge in edges:
            uf.union(edge[0], edge[1])

        return uf.connected(source, destination)

            
