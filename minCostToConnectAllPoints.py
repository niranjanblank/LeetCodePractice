"""
1584. Min Cost to Connect All Points
Medium
Topics
Companies
Hint
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
"""

class Solution1:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Time: O(n^2logn) : number of costs stored* time complexity for each pop
        # Space: O(n^2)
        #num of nodes
        N = len(points)
        # creating a adjacency  list to store the cost to reach the neighbor from the point
        adj = {i:[] for i in range(N)}

        # filling the adjacency list
        for i in range(N):
            x1,y1 = points[i]
            # we start j from i+1, to not include itself
            for j in range(i+1,N):
                x2, y2 = points[j]
                # calculate the manhattan dist
                dist = abs(x1-x2) + abs(y1-y2)
                # adding this to the adjacency list
                # from i we reach j
                adj[i].append([dist,j])
                # from j we reach i
                adj[j].append([dist ,i])

        # prims algorithm
        # starting with the node at index 0
        # minH stores all the possible paths from the current node,
        # minimum cost will be picked fom minH 
        minH = [[0,0]]
        visited = set()
        heapq.heapify(minH)
        res = 0
        while len(visited) < N:
            # pop the item with lowest cost
            min_cost, node = heappop(minH)
            # if the node is already in the visited set, we ignore rit
            if node in visited:
                continue

            res += min_cost
            visited.add(node)

            # visiting all the neighbourrs of the node
            for neigh_cost, neigh_node in adj[node]:
                if neigh_node not in visited:
                    # add it to minH to get the min cost in next loop
                    heappush(minH,[neigh_cost, neigh_node])

        return res            