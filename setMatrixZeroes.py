"""
"""


class Solution:
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(mn) solution
        # space O(mn) 
        # deep copy of matrix
        copy =  [row[:] for row in matrix]
        ROWS, COLS = len(copy), len(copy[0])
  
        for row in range(ROWS):
            for col in range(COLS):
                if copy[row][col] == 0:
                    for k in range(COLS):
                        # setting all the cols
                        matrix[row][k] = 0
                    for j in range(ROWS):
                        # setting all the matching rows
                        matrix[j][col] = 0

                
    def setZeroes2(self, matrix: List[List[int]]) -> None:
   # O(m+n) space solution
        ROWS, COLS = len(matrix), len(matrix[0])
        row_to_zero = [False] * ROWS
        col_to_zero = [False] * COLS
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    row_to_zero[row] =  True
                    col_to_zero[col] = True
        
        for row, value in enumerate(row_to_zero):
            if value:
                for col in range(COLS):
                    matrix[row][col] = 0

        for col, value in enumerate(col_to_zero):
            if value:
                for row in range(ROWS):
                    matrix[row][col] = 0


    def setZeroes3(self, matrix: List[List[int]]) -> None:
