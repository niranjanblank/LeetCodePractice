"""
1020. Number of Enclaves
Solved
Medium
Topics
Companies
Hint
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(mxn)
        # Space Complexity: O(mxn)
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            if (r < 0 or r >= m) or (c < 0 or c >= n ) or grid[r][c] == 0:
                return

            grid[r][c] = 0

            for dr, dc in directions:
                dfs(r+dr,c+dc)

        # we run dfs from the edges, and convert all the cells having 1 that are connected to the edges
        # with 1 in them
        for r in (0,m-1):
            for c in range(n):
                if grid[r][c]:
                    dfs(r,c)

        for r in range(m):
            for c in (0,n-1):
                 if grid[r][c]:
                    dfs(r,c)

        # we count the remaining land cells in the inner parts
        land_cells = 0
        for r in range(1,m):
            for c in range(1,n):
                if grid[r][c] == 1:
                    land_cells += 1
    
        return land_cells

                
