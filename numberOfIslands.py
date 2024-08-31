"""
200. Number of Islands
Medium
Topics
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # get the rows and cols
        ROWS, COLS = len(grid), len(grid[0])

        # using this variable we will store island count
        islands = 0

        def dfs(row, col):

            # if the row is water or is alreadu visited, we do nothing
            if (
                    # checking if the row,col values are in bound
                    row < 0 or row >= ROWS or
                    col < 0 or col >= COLS or
                    # checking if the row or col are already visited
                    grid[row][col] == "#" or
                    # checking if the the current location is water
                    grid[row][col] == "0"
            ):
                return

            # since its not visited, we mark it as visited by changing its value to "#"
            grid[row][col] = "#"
            # check all the for neighbouring cols
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(ROWS):
            for col in range(COLS):
                # checking if the current is land and isnt visited
                if grid[row][col] == "1":
                    # this means we found an unvisited island,
                    # now we increase the number of islands, and perform dfs to mark all neigbouring location as visited
                    islands += 1
                    dfs(row, col)
                    # once all the adjacent land are visited, we move to another iteration of loop

        return islands