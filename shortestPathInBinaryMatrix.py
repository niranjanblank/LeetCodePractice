"""
1091. Shortest Path in Binary Matrix
Solved
Medium
Topics
Companies
Hint
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        queue = deque()
        queue.append((0,0))
        grid[0][0] = 2
        n = len(grid)
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        length = 1
        while queue:
            for _ in range(len(queue)):
                curr_item = queue.popleft()

                 # If we reach the bottom-right cell, return the path length
                if curr_item[0] == n - 1 and curr_item[1] == n - 1:
                    return length

                for dx, dy in directions:
                    curr_x = dx + curr_item[0]
                    curr_y = dy + curr_item[1]

                    if  0 <= curr_x < n and 0 <= curr_y < n and grid[curr_x][curr_y] == 0:
                        queue.append((curr_x,curr_y))
                        grid[curr_x][curr_y] = 2
            length+=1
        
        return -1
                        
