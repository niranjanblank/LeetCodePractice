"""
1254. Number of Closed Islands
Solved
Medium
Topics
Companies
Hint
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            if (r < 0 or r >= m) or (c < 0 or c >= n) or grid[r][c] == 1:
                return
            
            # mark as visited
            grid[r][c] = 1

            for dr, dc in directions:
                dfs(r+dr, c+dc)

        # going around the edges and marking any land piece as visited, they wont contribute to closed islands
        for r in range(m):
            for c in (0,n-1):
                if grid[r][c] == 0:
                    dfs(r,c)
        
        for r in (0,m-1):
            for c in range(n):
                if grid[r][c] == 0:
                    dfs(r,c)

        # All the island at the edge wouldve been excluded by now 

        # running dfs in the inner section, and finding continous islands, they are part of closed island
        number_of_closed_islands = 0
        for r in range(1,m):
            for c in range(1,n):
                # if we find a piece of land, we increase the number of closed islands and we run dfs from it
                # to mark all other part of island as visited so as we dont visit them again
                if grid[r][c] == 0:
                    dfs(r,c)
                    number_of_closed_islands += 1

        return number_of_closed_islands
