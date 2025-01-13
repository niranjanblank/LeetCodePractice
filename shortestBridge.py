"""
934. Shortest Bridge
Solved
Medium
Topics
Companies
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(n^2)
        # Space Complexity: O(n^2)
        n = len(grid)
        queue = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        # dfs to get island

        def dfs(r,c):
            if not(0<= r <n and 0<= c <n) or grid[r][c] != 1 or (r,c) in visited: 
                return
            # add all the grid cells with value 1 to visited
            # doing this we will only have coordinates of all part of currernt island in set
            # so we wont visit them and end bfs later on
            visited.add((r,c))
            queue.append((r,c))
            # if we find a grid with 1, we add it to queue for bfs and search other 1s connected to it
            for dr,dc in directions:
                dfs(r+dr,c+dc)
            

        for ROW in range(n):
            for COL in range(n):
                if grid[ROW][COL] == 1:
                    dfs(ROW,COL)
                    break
            # exit the loop once the first island is found 
            if len(queue) > 0:
                break
        
        print(queue)
        flips = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    curr_r,curr_c = r+dr, c+dc
                    if 0 <= curr_r < n and 0 <= curr_c < n and (curr_r,curr_c) not in visited:
                        if grid[curr_r][curr_c] == 0:
                                # marks the cell as visited
                                visited.add((curr_r,curr_c))
                                queue.append((curr_r, curr_c))
                        elif grid[curr_r][curr_c] == 1:
                            return flips  # Found the second island

            flips += 1
        return flips
