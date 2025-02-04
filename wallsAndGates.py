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





"""

Submissions
Submissions


Code
Testcase
Test Result
Test Result
286. Walls and Gates
Solved
Medium
Topics
Companies
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
 

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.

"""

class Solution2:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])

        queue = deque()
        # directions to go four ways from a position
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # storing the locations of gates
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    queue.append((r,c))

        distance = 0
        while queue:

            for _ in range(len(queue)):
                r,c = queue.popleft()

                

                if  rooms[r][c] == 2**31 - 1:
                    rooms[r][c] = distance

                # going through all the possible paths
                for dr, dc in directions:
                    curr_r = r + dr
                    curr_c = c + dc

                    if ((0 <= curr_r < m) and
                    (0 <= curr_c < n) and
                    rooms[curr_r][curr_c] == 2**31 - 1):
                        queue.append((curr_r,curr_c))

            distance +=1

