"""
70. Climbing Stairs
Easy
Topics
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def dfs(total):
            # If we reach exactly n steps, this is a valid way
            if total == n:
                return 1

            # If we exceed n steps, this is not a valid way
            if total > n:
                return 0

            # Check if the result for the current total steps is already computed
            if total in memo:
                return memo[total]

            # Recursively calculate the number of ways by taking 1 step or 2 steps
            memo[total] = dfs(total + 1) + dfs(total + 2)
            return memo[total]

        # Start the recursion from step 0
        return dfs(0)

# dynamic prrogrramming
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one