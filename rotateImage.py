"""
48. Rotate Image
Medium
Topics
Companies
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the input matrix 90 degrees clockwise in-place.
        """
        # Initialize the left and right boundaries of the matrix.
        # Left starts at the first column, and right starts at the last column.
        left, right = 0, len(matrix[0]) - 1

        # Continue rotating layers until all layers have been processed.
        while left < right:

            # Iterate over elements in the current layer (top row) that need to be rotated.
            # For each outer layer, n elements require n-1 rotations.
            for i in range(right - left):
                # Set the top and bottom boundaries for this layer.
                top, bottom = left, right

                # Store the top-left element temporarily to use it later for rotation.
                temp = matrix[top][left + i]

                # Move the bottom-left element to the top-left position.
                matrix[top][left + i] = matrix[bottom - i][left]

                # Move the bottom-right element to the bottom-left position.
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Move the top-right element to the bottom-right position.
                matrix[bottom][right - i] = matrix[top + i][right]

                # Move the temporarily stored top-left element to the top-right position.
                matrix[top + i][right] = temp

            # Move inwards to process the next inner layer.
            left += 1
            right -= 1