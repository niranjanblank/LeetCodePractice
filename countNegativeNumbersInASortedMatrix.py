"""
1351. Count Negative Numbers in a Sorted Matrix
Solved
Easy
Topics
Companies
Hint
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.



Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100


Follow up: Could you find an O(n + m) solution?
"""


class Solution:
    # time complexity O(nxm)
    def countNegatives(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        total_negatives = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] < 0:
                    total_negatives += COLS - j
                    break

        return total_negatives

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        row, col = 0, COLS - 1
        total_negatives = 0

        while row < ROWS and col >= 0:
            # If the current element is negative, all elements below in this column are negative
            if grid[row][col] < 0:
                total_negatives += ROWS - row  # Add all elements in this column from this row downward
                col -= 1  # Move left to check smaller elements in the same row
            else:
                row += 1  # Move down to the next row to check larger elements

        return total_negatives

