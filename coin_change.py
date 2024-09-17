"""
322. Coin Change
Solved
Medium
Topics
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top-down memoization solution using Depth-First Search (DFS) with caching
        # cache stores the minimum number of coins needed for each remaining amount
        cache = {}

        def dfs(remaining):
            # Base case: if remaining amount is 0, no more coins are needed
            if remaining == 0:
                return 0
            # If remaining amount is negative, it's impossible to form that amount with the given coins
            if remaining < 0:
                return float('inf')

            # If the result for this remaining amount has already been computed, return it from cache
            if remaining in cache:
                return cache[remaining]

            # Initialize the minimum number of coins needed to an infinite value
            min_coins = float('inf')
            # Try using each coin and recursively calculate the minimum coins needed for the remaining amount
            for coin in coins:
                # Recursive call: subtract the coin value from the remaining amount
                result = 1 + dfs(remaining - coin)
                # Update min_coins if the current path results in fewer coins
                min_coins = min(min_coins, result)

            # Store the computed result for the current remaining amount in the cache
            cache[remaining] = min_coins

            return cache[remaining]

        # Start DFS with the target amount. If the result is infinity, it means no valid solution was found.
        res = dfs(amount)

        # Return -1 if no solution was found (res is still infinity), otherwise return the minimum number of coins
        return res if res != float('inf') else -1


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize a dynamic programming (dp) array where each index represents the minimum
        # number of coins needed to make up that amount. Set all values to amount + 1 (an
        # impossible large number) as the initial default, since this is greater than any
        # possible number of coins we could need. The size of dp is amount + 1 to include 0.
        dp = [amount + 1] * (amount + 1)

        # Base case: no coins are needed to make amount 0, so dp[0] is set to 0.
        dp[0] = 0

        # Iterate over each amount from 1 to the target amount, and for each, determine the
        # minimum number of coins needed to make that amount.
        for a in range(1, amount + 1):
            # For each coin, check if it can contribute to the current amount 'a'. If the coin's
            # value is less than or equal to 'a', we can subtract the coin's value from 'a'
            # and update dp[a] to be the minimum of its current value or the value of dp[a - coin] + 1
            # (which represents using one additional coin).
            for coin in coins:
                # If the coin can be used (i.e., a - coin >= 0), update dp[a] to the minimum number
                # of coins needed by comparing the current dp[a] with 1 + dp[a - coin].
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        # After filling the dp array, check if the target amount has been updated. If it is still
        # the initial large value (amount + 1), that means it's impossible to form the amount with
        # the given coins, so return -1. Otherwise, return dp[amount], which gives the minimum number
        # of coins required to form the target amount.
        return dp[amount] if dp[amount] != amount + 1 else -1



