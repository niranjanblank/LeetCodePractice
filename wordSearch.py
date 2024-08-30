"""

Code
Testcase
Test Result
Test Result
79. Word Search
Medium
Topics
Companies
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board, board[0])

        # To keep track of the letters we have visited in the board, so as not to revisit them
        path = set()

        def dfs(r, c, i):
            # If we have reached the length of the word, it means we have successfully matched all characters.
            # At this point, i == len(word) indicates that there are no more characters left to match in the word,
            # so we return True to signal that the entire word has been found in the board.
            if i == len(word):
                return True

            # Checking out-of-bounds condition or
            # if the letter at location [r, c] isn't equal to the word at index [i]
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i] or
                (r, c) in path
            ):
                return False

            # If we don't reach the above conditions, then we proceed
            # At this point, we have found a letter from the word at (r, c)
            # so let's add it to the path
            path.add((r, c))

            # Now we check for the next letter at top, down, left, and right
            # If we get True for any of these paths, we have found a letter that matches the letter in the word
            res = (
                dfs(r - 1, c, i + 1) or
                dfs(r + 1, c, i + 1) or
                dfs(r, c - 1, i + 1) or
                dfs(r, c + 1, i + 1)
            )

            # Backtrack: We need to remove the current cell from the path set
            # because we are done exploring all possible paths starting from this cell.
            # This allows the cell to be reused in other potential paths as the path set
            # should only track the current path being explored, not all previously explored cells.
            path.remove((r, c))

            return res

        # Now for each item in the board, run this dfs to find the path
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False