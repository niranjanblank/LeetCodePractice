"""
695. Max Area of Island
Solved
Medium
Topics
Companies
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # get the rows and cols
        ROWS, COLS = len(grid), len(grid[0])

        # store the max_are in this variable
        max_area = 0

        def dfs(row, col):
            # checking if the cell is already visited
            # or if its out of bounds
            if (
                    row < 0 or row >= ROWS or
                    col < 0 or col >= COLS or
                    grid[row][col] == "#" or
                    grid[row][col] == 0
            ):
                return 0

            # if we reach here, it means we have found land, so we give it an area of 1
            area = 1
            # mark it as visited
            grid[row][col] = '#'

            # find other adjacent land and add its area to it
            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)

            return area

        # going through all the rows and cols
        for row in range(ROWS):
            for col in range(COLS):
                # if we find land, we calculate its area
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area

