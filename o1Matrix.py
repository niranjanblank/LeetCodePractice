"""
542. 01 Matrix
Solved
Medium
Topics
Companies
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
 

Note: This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        m = len(mat)
        n = len(mat[0])
        output = [[0]*n for i in range(m)]
        queue = deque()
        # first pass to store the position of  0s

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    mat[i][j] = -1
                    queue.append((i,j))

        path = 1

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue:
            for _ in range(len(queue)):
                cell_r, cell_c = queue.popleft()

                for dr,dc in directions:
                    curr_r = cell_r + dr
                    curr_c = cell_c + dc

                    if (0 <= curr_r < m) and (0 <= curr_c <n):
                        if mat[curr_r][curr_c] != -1:
                            # mark as visited
                            mat[curr_r][curr_c] = -1
                            output[curr_r][curr_c] = path
                            queue.append((curr_r,curr_c))
            path+=1
        # second pass

        return output
