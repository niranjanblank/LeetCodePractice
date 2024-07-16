"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    ROWS, COLS = len(matrix), len(matrix[0])
    top, bot = 0, ROWS - 1
    while top <= bot:
        row = (top+bot)//2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row -1
        else:
            break

    if top > bot:
        return False


    row = (top + bot) // 2

    l,r = 0, len(matrix[row])-1
    while l<=r:
        mid = (l+r)//2

        if target == matrix[row][mid]:
            return True
        elif target > matrix[row][mid]:
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid -1

    return False


print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))