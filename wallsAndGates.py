"""
Islands and Treasure
You are given a
m
×
n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}
"""
from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # getting rows and cols
        ROWS, COLS = len(grid), len(grid[0])

        # for implementing bfs, we need queue
        queue = deque()

        # to keep track of visited gates
        visited = set()

        def add_room(row, col):
            if (row < 0 or row == ROWS or col < 0 or col == COLS or
                    (row, col) in visited or grid[row][col] == -1):
                return

            queue.append([row, col])
            visited.add((row, col))

        # going through every rows and finding out the gates
        for r in range(ROWS):
            for c in range(COLS):
                # means we found the gates, and now append it to the queue to be used in BFS
                if grid[r][c] == 0:
                    queue.append([r, c])
                    # marks as visited
                    visited.add((r, c))

        # indicates distance from the gates
        dist = 0

        # running the BFS
        while queue:
            # this will run through all the gates first, and then move to next level
            for i in range(len(queue)):
                row, col = queue.popleft()

                grid[row][col] = dist

                # adding four neighbours to the queue
                add_room(row + 1, col)
                add_room(row - 1, col)
                add_room(row, col + 1)
                add_room(row, col - 1)

            # increasing the distance for next levels
            dist += 1