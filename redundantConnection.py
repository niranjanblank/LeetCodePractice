"""
684. Redundant Connection
Medium
Topics
Companies
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.



Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]


Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # initially each nodes is its own parent
        # we will ignorent parent[0] as trees have nodes frrom 1 to n only
        parent = [i for i in range(len(edges) + 1)]
        # initially rank of each parent is 1
        rank = [1] * len(parent)

        def find(n):
            """This function finds the parent of node n"""
            p = parent[n]

            # finding the root parent
            while p != parent[p]:
                # path compression
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        def union(n1, n2):
            """
            This function merges two nodes if they arent merged,and returns True
            else, it return false
            """
            # finding the parents of n1, n2
            p1 = find(n1)
            p2 = find(n2)

            # if the parernts of n1, and n2 is same, then joining them creates a loop, so return False
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                # if the rank of p1 is greater than p2, parent of p2 is set to p1
                parent[p2] = p1
                # increase the rank fo p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            # if we fail to perfom the union, then it means this is additional edge and creates cycle
            if not union(n1, n2):
                return [n1, n2]
