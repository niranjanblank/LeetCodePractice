"""
1926. Nearest Exit from Entrance in Maze
Solved
Medium
Topics
Companies
Hint
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

 

Example 1:


Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:


Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
Example 3:


Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
"""

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Time Complexity: O(mxn)
        # Space complexity: O(mxn) 
        queue = deque()
        # add the entrance to the queue
        queue.append(entrance)
        m = len(maze)-1
        n = len(maze[0])-1
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        maze[entrance[0]][entrance[1]] = "+" 
        steps = 0
        while queue:
            # we process all the elements at a level at once using this loop
            for _ in range(len(queue)):
                pos = queue.popleft()
                for dx,dy in direc:
                    curr_x = pos[0] + dx
                    curr_y = pos[1] + dy

                    if (curr_x <= m and curr_x >= 0) and (curr_y <=n and curr_y >=0):
                        if  maze[curr_x][curr_y] == ".":
                            # mark the cell as visited
                            maze[curr_x][curr_y] = "+"
                            # we found empty cell
                            # if we find the exit return the steps
                            if (curr_x == m or curr_x == 0) or  (curr_y == n or curr_y==0):
                                return steps + 1
                            else:
                                queue.append([curr_x,curr_y])
                        elif maze[curr_x][curr_y] == "+":
                            continue
            # increment steps after processing all the cells at current step
            steps +=1

        # return -1 if path cannot be found
        return -1
