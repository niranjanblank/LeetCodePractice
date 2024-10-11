"""

441. Arranging Coins
Solved
Easy
Topics
Companies
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
 

Constraints:

1 <= n <= 231 - 1
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # here in this case, we could have a maximum of n rows
        # as we have n coin
        # to store maximum number of complete rows of coins
        res = 0
        l,r = 1, n
        while l <= r:
            m = (l+r)//2
            # total coins required at m
            total = m * (m+1) //2
            if total < n:
                # if this is true, we might find better result in the right section
                l = m + 1
                res = m
            elif total == n:
                # this is the best result we can achieve
                return m
            else:
                r = m - 1
        
        return res
