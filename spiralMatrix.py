"""
54. Spiral Matrix
Medium
Topics
Companies
Hint
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # left to right
            for i in range(left, right):
                res.append(matrix[top][i])

            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])

            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])

            left += 1

        return res


class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        # setting the boundaries
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while left <= right and top <= bottom:
            # transverse left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            # this means the top row has been completed
            # so update the top pointer
            top += 1

            # transverse top to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            # this means rightmost column has been completed
            # so update right pointer
            right -= 1

            if not (left <= right and top <= bottom):
                break

            # transverse right to left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])

            # this means bottom column has been completed
            # so update bottom pointer
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])

            left += 1

        return res