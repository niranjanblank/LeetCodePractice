"""
1059. All Paths from Source Lead to Destination
Solved
Medium
Topics
Companies
Hint
Given the edges of a directed graph where edges[i] = [ai, bi] indicates there is an edge between nodes ai and bi, and two nodes source and destination of this graph, determine whether or not all paths starting from source eventually, end at destination, that is:

At least one path exists from the source node to the destination node
If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
The number of possible paths from source to destination is a finite number.
Return true if and only if all roads from source lead to destination.

 

Example 1:


Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
Output: false
Explanation: It is possible to reach and get stuck on both node 1 and node 2.
Example 2:


Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
Output: false
Explanation: We have two possibilities: to end at node 3, or to loop over node 1 and node 2 indefinitely.
Example 3:


Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
Output: true
 

Constraints:

1 <= n <= 104
0 <= edges.length <= 104
edges.length == 2
0 <= ai, bi <= n - 1
0 <= source <= n - 1
0 <= destination <= n - 1
The given graph may have self-loops and parallel edges.
"""

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])


        visited = set()
        # processed = set()
        memo = {}
        def dfs(node):
            if node in visited:
                # we have a cycle, so return False
                return False
            if node in memo:
                # if node is memo, we know if the node will reach destination or not
                return memo[node]
            if len(adj[node])== 0:
                # if we reach a leaf with no outgoing edges, we check if it is destination
                return node == destination
            visited.add(node)
            # going through all the neigh
            for nei in adj[node]:
                if not dfs(nei):
                    # any any path return false, we return false
                    # this node wont even reach destination
                    memo[node]= False
                    return False
            
            # after dfs is completed for the node, remove it
            visited.remove(node)
            # if we reach here, it means all the paths are valid from this node to dest, so add this to memo and mark it as true
            memo[node]= True

            return True

        # Destination should not have outgoing edges
        if adj[destination]:
            return False
        
        return dfs(source)
