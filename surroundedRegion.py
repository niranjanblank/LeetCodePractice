"""
130. Surrounded Regions
Medium
Topics
Companies
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.



Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]



Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        # finding the outer regions, since they cannot be surrounded

        def dfs(r, c):
            if (
                    r < 0 or c < 0 or
                    c == COLS or r == ROWS or
                    board[r][c] != "O"
            ):
                return

            # converting the found region to some temporary value
            board[r][c] = "*"
            # checking all the surrounding areas
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (
                        (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and
                        board[r][c] == "O"
                ):
                    dfs(r, c)
        # convert all other remaining "O" to "X" as they can be surrounded by "X"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # converting the outer regions back to "O"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "*":
                    board[r][c] = "O"