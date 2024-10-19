"""
62. Unique Paths
Solved
Medium
Topics
Companies
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
"""


class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # all the position in the last row will be of value 1
        row = [1] * n

        # loop through all other rows
        # we are calculating row from bottom to top
        for i in range(m-1):       
            # this is supposed to be the value of the current row in loop
            newRow = [1] * n
            for j in range(n-2,-1,-1):
                # its value is calculated as sum of right and down pos
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        # memoization
        # to store ways to reach finish from this point
        cache = {}
        def dfs(r,c):
            # since the last column and last row will all have 1 value
            if r == m -1 or c == n-1:
                return 1
            # check if the value is in the cache
            if (r,c) in cache:
                return cache[(r,c)]
            
            # if we reach here, it means the value isnt in the cache yet so calculate the ways
            # store the ways to reach for (r,c) to finish in the cache
            cache[(r,c)] = dfs(r,c+1) + dfs(r+1,c)
            # return the value
            return cache[(r,c)]
        # get the total paths to reach finish from 0,0
        ans = dfs(0,0)
        return ans
