"""
778. Swim in Rising Water
Solved
Hard
Topics
Companies
Hint
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

Example 1:


Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:


Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        # add the first item of grid 
        minHeap = [(grid[0][0],0,0)] # elevation, row, col
        heapq.heapify(minHeap)
        # add its to the visited set
        visited.add((0,0))

        # directions to reach all the adjacent grid places
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            # if we have reached the last position of grid, return the path
            if r == N-1 and c == N-1:
                return t

            # if not, we run the djikstras on the adjacent grid cells
            for dr, dc in directions:
                # coordinates of neighbours
                neiR = r + dr
                neiC = c + dc
                # check if the coorrdinates are already visited and in bounds
                if (((neiR,neiC) in visited) or
                (neiR < 0 or neiC < 0) or
                (neiR == N or neiC == N)):
                    continue
                visited.add((neiR, neiC))
                # add it to the minHeap
                # the elevation value to be added to the heap should be maximum elevation upto that point
                heapq.heappush(minHeap, (max(t, grid[neiR][neiC]),neiR, neiC))

